#!/usr/bin/env python3
"""Independent, reproducible checks; none of these numerical checks is a proof.

Requirements: Python 3.10+, mpmath, sympy.
Run: python verify.py --output verification_results.json
The mathematical proofs are in manuscript.tex and proof_notes.md.
"""

import argparse
import json
import time
from pathlib import Path

import mpmath as mp
import sympy as sp


class CheckFailure(RuntimeError):
    pass


def check(condition, message="check failed"):
    """Explicit check that is not removed under python -O."""
    if not condition:
        raise CheckFailure(message)



def moments(a, z, count):
    """Bessel transform plus the Pearson recurrence, at arbitrary precision."""
    a, z = mp.mpf(a), mp.mpc(z)
    if not z:
        return [mp.beta(mp.mpf(j + 1) / 2, a + 1) if j % 2 == 0 else mp.mpf(0)
                for j in range(count)]
    nu = a + mp.mpf('0.5')
    scale = mp.sqrt(mp.pi) * mp.gamma(a + 1) * (2 / z) ** nu
    out = [scale * mp.besselj(nu, z)]
    if count > 1:
        out.append(1j * scale * mp.besselj(nu + 1, z))
    for k in range(count - 2):
        previous = out[k - 1] if k else 0
        out.append(out[k] + (k * previous - (k + 2 * a + 2) * out[k + 1]) / (1j * z))
    return out


def moment_hyper(a, z, j):
    """An independent power-series expression, without the Pearson recurrence."""
    a, z = mp.mpf(a), mp.mpf(z)
    if j % 2 == 0:
        c = mp.mpf(j + 1) / 2
        return mp.beta(c, a + 1) * mp.hyper([c], [mp.mpf('.5'), c + a + 1], -z*z/4)
    c = mp.mpf(j + 2) / 2
    return 1j * z * mp.beta(c, a + 1) * mp.hyper([c], [mp.mpf('1.5'), c + a + 1], -z*z/4)


def determinant(a, z, n):
    if n == 0:
        return mp.mpf(1)
    mu = moments(a, z, 2*n - 1)
    return mp.det(mp.matrix([[mu[j+k] for k in range(n)] for j in range(n)]))


def zero_frequency(a, n):
    return 2 ** (n * (2*a + n)) * mp.fprod(
        mp.factorial(j) * mp.gamma(a+j+1)**2 / mp.gamma(2*a+n+j+1)
        for j in range(n))


def tail_constant(a, r):
    return 2 ** (2*r*(a+r)) * mp.fprod(
        (mp.factorial(j) * mp.gamma(a+j+1))**2 for j in range(r))


def polynomial_moments(lam, u, count):
    out = [sp.S.One, -2*lam]
    for k in range(count - 2):
        previous = out[k-1] if k else 0
        out.append(sp.expand(-u*out[k] - (k+2*lam+1)*out[k+1] - k*u*previous))
    return out[:count]


def polynomial_determinant(p, n, shifted=False):
    if not n:
        return sp.S.Zero if shifted else sp.S.One
    cols = list(range(n-1)) + [n if shifted else n-1]
    dm = sp.polys.matrices.DomainMatrix.from_Matrix(
        sp.Matrix([[p[j+k] for k in cols] for j in range(n)]))
    return sp.expand(dm.domain.to_sympy(dm.det()))


def expected_leading(lam, n):
    r = n // 2
    def K(m):
        return sp.prod(sp.factorial(j)*sp.rf(lam+sp.Rational(1,2),j) for j in range(m))
    if n % 2 == 0:
        return (-1)**r * 2**(2*r*(r-1)) * K(r)**2
    return 2**(2*r*r) * K(r)*K(r+1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='verification_results.json')
    args = parser.parse_args()
    start = time.time()
    mp.mp.dps = 90
    results = {'precision_decimal_digits': mp.mp.dps,
               'purpose': 'Sanity checks and exact algebraic verification; not a numerical proof.'}

    # Independent moment formulas check the recurrence and all complex phases.
    errors = []
    for a, z in [('-0.99', '.7'), ('0', '2.3'), ('1.4142135623730950488', '11')]:
        mu = moments(a, z, 12)
        for j in range(12):
            other = moment_hyper(a, z, j)
            errors.append(abs(mu[j]-other)/max(1,abs(other)))
    check(max(errors) < mp.mpf('1e-65'), "max(errors) < mp.mpf('1e-65')")
    results['independent_moment_formula_max_scaled_error'] = mp.nstr(max(errors), 8)

    # A deliberately limited grid covers a near-singular endpoint, a noninteger
    # exponent, the origin, oscillations, and a high-frequency tail.
    numerical = []
    for a in ['-0.99', '-0.5', '0', '0.5', '1.4142135623730950488', '3']:
        for z in ['0', '.1', '3.1415926535897932384626433832795028841971693993751', '10', '50']:
            for n in [2, 4, 6, 8]:
                value = determinant(a, z, n)
                check(abs(mp.im(value)) < mp.mpf('1e-65') * max(1,abs(value)), "abs(mp.im(value)) < mp.mpf('1e-65') * max(1,abs(value))")
                check(mp.re(value) > 0, repr((a, z, n, mp.nstr(value, 50))))
                numerical.append({'alpha': a, 'omega': z, 'size': n,
                                  'determinant': mp.nstr(mp.re(value), 20)})
    results['even_determinant_checks'] = numerical

    origin_errors = []
    for a in [mp.mpf('-.9'), mp.mpf(0), mp.mpf('1.5')]:
        for n in [1, 2, 4, 6]:
            exact = zero_frequency(a, n)
            origin_errors.append(abs(determinant(a, 0, n)/exact-1))
    check(max(origin_errors) < mp.mpf('1e-70'), "max(origin_errors) < mp.mpf('1e-70')")
    results['selberg_origin_max_relative_error'] = mp.nstr(max(origin_errors), 8)

    known_errors = []
    for z in [mp.mpf('.1'), mp.pi, mp.mpf(50)]:
        known = 4*(z*z-mp.sin(z)**2)/z**4
        known_errors.append(abs(determinant(0,z,2)/known-1))
    check(max(known_errors) < mp.mpf('1e-70'), "max(known_errors) < mp.mpf('1e-70')")
    results['alpha_zero_D2_max_relative_error'] = mp.nstr(max(known_errors), 8)

    tails = []
    for a in [mp.mpf('-.8'), mp.mpf('.5'), mp.mpf(2)]:
        for r in [1,2,3]:
            for z in [mp.mpf(100), mp.mpf(1000)]:
                ratio = determinant(a,z,2*r) * z**(2*r*(a+r))/tail_constant(a,r)
                tails.append({'alpha':str(a),'size':2*r,'omega':str(z),
                              'ratio_to_leading_asymptotic':mp.nstr(mp.re(ratio),20)})
    results['tail_constant_checks'] = tails

    toda = []
    a, z = mp.mpf('.7'), mp.mpf('2.3')
    for n in range(1,7):
        f = lambda w: determinant(a,w,n)
        d, d1, d2 = f(z), mp.diff(f,z,1), mp.diff(f,z,2)
        rhs = determinant(a,z,n-1)*determinant(a,z,n+1)
        error = abs(d*d2-d1*d1+rhs)/max(abs(rhs),abs(d*d2),abs(d1*d1))
        check(error < mp.mpf('1e-65'), "error < mp.mpf('1e-65')")
        toda.append({'size':n,'scaled_residual':mp.nstr(error,8)})
    results['toda_checks'] = toda

    u, lam = sp.symbols('u lambda')
    p = polynomial_moments(lam,u,11)
    hs = {0:sp.S.One}
    degree_checks = []
    for n in range(1,6):
        h = polynomial_determinant(p,n)
        hs[n] = h
        poly = sp.Poly(h,u)
        check(poly.degree() == n*n//4, 'poly.degree() == n*n//4')
        check(sp.simplify(poly.LC()-expected_leading(lam,n)) == 0, 'sp.simplify(poly.LC()-expected_leading(lam,n)) == 0')
        degree_checks.append({'size':n,'degree':poly.degree(),'leading_coefficient':str(sp.factor(poly.LC()))})
    results['formal_degree_and_leading_coefficient_checks'] = degree_checks

    numerator_checks = []
    for n in range(0,5):
        sharp = polynomial_determinant(p,n,True)
        sharp_next = polynomial_determinant(p,n+1,True)
        v = sp.Poly(sp.expand(sharp*hs[n+1]-sharp_next*hs[n]),u)
        r = n//2
        alpha = lam-sp.Rational(1,2)
        c = ((r+2)*alpha+r*r+3*r+1) if n%2==0 else (1+r-r*r-r*alpha)
        check(v.degree() == n*(n+1)//2, 'v.degree() == n*(n+1)//2')
        check(sp.simplify(v.LC()-c*expected_leading(lam,n)*expected_leading(lam,n+1)) == 0, 'sp.simplify(v.LC()-c*expected_leading(lam,n)*expected_leading(lam,n+1)) == 0')
        numerator_checks.append({'index':n,'formal_degree':v.degree(),'leading_coefficient':str(sp.factor(v.LC()))})
    results['shifted_numerator_checks'] = numerator_checks

    # The full 2026 Conjecture 2.5 additionally requires correctly normalised
    # shifted-column residual polynomials. These check their zero-frequency
    # cancellation and leading coefficients independently at low rank.
    residual_checks=[]
    for n in range(2,6):
        sharp=polynomial_determinant(p,n,True)
        numerator=sp.Poly(sharp+n*(2*lam+n-1)*hs[n],u)
        quotient,remainder=sp.div(numerator,sp.Poly(u,u))
        check(remainder.is_zero, 'remainder.is_zero')
        r=n//2
        e=r*(2*lam+2*r-1) if n%2==0 else sp.Rational(r,2)*(2*lam+2*r+1)
        check(quotient.degree()==n*n//4-1, 'quotient.degree()==n*n//4-1')
        check(sp.simplify(quotient.LC()-expected_leading(lam,n)*e)==0, 'sp.simplify(quotient.LC()-expected_leading(lam,n)*e)==0')
        residual_checks.append({'size':n,'degree':quotient.degree(),
                                'normalised_polynomial':str(sp.factor(quotient.as_expr()/(expected_leading(lam,n)*e)))})
    results['conjecture_2_5_shifted_residuals']=residual_checks

    # The lambda=0 reduction behind Conjecture 2.7 has an exact zero of order
    # n-1 at u=0 and a shifted ratio controlled by a Laguerre measure plus an
    # atom. Check these statements through size nine using exact arithmetic.
    pp=polynomial_moments(sp.S.Zero,u,20)
    reduced_checks=[]
    for n in range(2,10):
        h=polynomial_determinant(pp,n)
        sh=polynomial_determinant(pp,n,True)
        rh,rem=sp.div(sp.Poly(h,u),sp.Poly(u**(n-1),u))
        rsh,remsh=sp.div(sp.Poly(sh,u),sp.Poly(u**(n-1),u))
        check(rem.is_zero and remsh.is_zero and rh.eval(0)!=0, 'rem.is_zero and remsh.is_zero and rh.eval(0)!=0')
        B=sp.Integer(n*(n-1))
        A=B**2/(B+2)
        check(sp.simplify(rsh.eval(0)/rh.eval(0)+A)==0, 'sp.simplify(rsh.eval(0)/rh.eval(0)+A)==0')
        s=n*n//4-n+1
        check(rh.degree()==s, 'rh.degree()==s')
        e=A-B/2 if n%2==0 else A-3*B/4
        if n>=4:
            q,remq=sp.div(rsh+A*rh,sp.Poly(u,u))
            check(remq.is_zero and q.degree()==s-1, 'remq.is_zero and q.degree()==s-1')
            check(sp.simplify(q.LC()/rh.LC()-e)==0, 'sp.simplify(q.LC()/rh.LC()-e)==0')
        reduced_checks.append({'size':n,'valuation':n-1,'reduced_degree':s,
                               'negative_constant_ratio':str(A),
                               'leading_residual_ratio':str(e)})
    results['conjecture_2_7_reduced_checks']=reduced_checks

    exceptions=[]
    for n, lv in [(3,sp.Rational(3,2)),(5,sp.S.Zero)]:
        pp=polynomial_moments(lv,u,2*n+2)
        h=polynomial_determinant(pp,n)
        hn=polynomial_determinant(pp,n+1)
        v=sp.Poly(polynomial_determinant(pp,n,True)*hn-polynomial_determinant(pp,n+1,True)*h,u)
        check(v.degree()==n*(n+1)//2-1, 'v.degree()==n*(n+1)//2-1')
        exceptions.append({'index':n,'lambda':str(lv),'degree':v.degree(),'factored_polynomial':str(sp.factor(v.as_expr()))})
    results['exceptional_specialisations']=exceptions

    # Exact measure counterexample: the oscillatory factors at 2*pi are +/-1.
    atoms=[sp.Rational(-1),sp.Rational(-1,2),sp.S.Zero,sp.Rational(1,2),sp.S.One]
    weights=[sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,6)]
    phases=[1,-1,1,-1,1]
    mu=[sum(w*ph*t**j for t,w,ph in zip(atoms,weights,phases)) for j in range(7)]
    d2=sp.det(sp.Matrix(2,2,lambda j,k:mu[j+k]))
    d4=sp.det(sp.Matrix(4,4,lambda j,k:mu[j+k]))
    check(d2==sp.Rational(1,12) and d4==sp.Rational(-1,1536), 'd2==sp.Rational(1,12) and d4==sp.Rational(-1,1536)')
    results['symmetric_measure_counterexample']={'moments':[str(v) for v in mu], 'D2':str(d2),'D4':str(d4)}

    # Prior-claim check (Section 9): at a zero zeta of J_{lambda-1}, the all-entry
    # shifted ratio zeta*mu_1/mu_0 equals 2i*lambda, so the printed formula gives a
    # non-real u_1 when lambda != 0; and D_n^{(1)} is purely imaginary for odd n.
    prior=[]
    for lam in [mp.mpf('1.25'), mp.mpf('1.5'), mp.mpf('3.75')]:
        a=lam-mp.mpf('0.5')
        zeta=mp.besseljzero(lam-1,1)
        mu=[moment_hyper(a,zeta,j) for j in range(8)]
        ratio=zeta*mu[1]/mu[0]
        check(abs(ratio-2j*lam)<mp.mpf('1e-60'), 'ratio 2i lambda')
        for n in [1,3]:
            dshift=mp.det(mp.matrix([[mu[i+j+1] for j in range(n)] for i in range(n)]))
            dn=mp.det(mp.matrix([[mu[i+j] for j in range(n)] for i in range(n)]))
            check(abs(mp.re(dshift))<mp.mpf('1e-60')*max(1,abs(dshift)), 'shifted det imaginary')
            check(abs(mp.im(dn))<mp.mpf('1e-60')*max(1,abs(dn)), 'D_n real')
        prior.append({'lambda':str(lam),'zeta':mp.nstr(zeta,30),'zeta_mu1_over_mu0':mp.nstr(ratio,30)})
    results['prior_claim_formula_check']=prior

    # Negative control: the checker must reject a deliberately wrong tail constant.
    try:
        check(abs(tail_constant(mp.mpf('0.7'),1)*1.01-tail_constant(mp.mpf('0.7'),1))<mp.mpf('1e-30'), 'negative control')
        raise SystemExit('negative control was not rejected')
    except CheckFailure:
        results['negative_control']='wrong tail constant rejected'

    results['elapsed_seconds']=round(time.time()-start,3)
    results['status']='all checks passed'
    Path(args.output).write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'status':results['status'],'numerical_even_cases':len(numerical),
                      'symbolic_H_sizes':len(degree_checks),'elapsed_seconds':results['elapsed_seconds'],
                      'output':str(Path(args.output).resolve())},indent=2))


if __name__=='__main__':
    main()
