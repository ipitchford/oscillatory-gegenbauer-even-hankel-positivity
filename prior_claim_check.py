"""Checks of the formulas in Ashfaque (2026), read in full (see competing_claim_audit.md).

Part 1 (SymPy, exact): the change of variables of its Theorem 2.2 maps equations (3)-(4) to (6)-(7).
Part 2 (mpmath, 40 digits): at Bessel zeros, residuals of (3)-(4); the true u_n against its equation (8)
and against the difference formula in its proof; its equation (9) with tau_n = D_n against the Toda identity.
Usage: python -I -B prior_claim_check.py > prior_claim_check.json
"""
import sympy as s
n,l,z,a0,a1,b0,b1,b2=s.symbols('n lambda zeta a0 a1 b0 b1 b2')
c=2*n+1+2*l
a1e=s.Rational(3,2)/z*c-a0+c/(2*z*b1)*(b0-1+a0*((2*n-1+2*l)/z-a0))
b2e=b0+a1**2-a0**2+(a0*(2*n-1+2*l)-a1*(2*n+3+2*l))/z
u=lambda a,k: z*a-(2*k+2*l-1)
v=lambda b: z**2*b
u0,u1,v0,v1,v2=u(a0,n),u(a1e,n+1),v(b0),v(b1),v(b2e)
e6=s.simplify(u1+u0-((3-2*n-2*l)/2+(2*n+2*l+1)/(2*v1)*(v0-z**2-u0**2-(2*n+2*l-1)*u0)))
U1=u(a1,n+1)
e7=s.simplify(v2-v0-(U1**2-u0**2+(2*n+2*l-1)*(U1-u0)-2*(2*n+2*l+1)))
assert_exact = (s.simplify(e6) == 0 and s.simplify(e7) == 0)
if not assert_exact: raise SystemExit("change of variables check failed")
import mpmath as mp, json, sys
mp.mp.dps = 40
def moments(lam, z, K):
    a = lam - mp.mpf(1)/2
    # exact: mu_k = i^k d^k/dz^k of mu_0(z), mu_0 = pi*Gamma(a+1)*(2/z)^(lam) J_lam(z)... use quadrature
    return [mp.quad(lambda x: x**k*(1-x**2)**a*mp.expj(z*x), [-1,0,1]) for k in range(K)]
def H(mu, n, shift=0, lastcol=False):
    if n == 0: return mp.mpf(1)
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            if lastcol: M[i,j] = mu[i+j+(1 if j==n-1 else 0)]
            else: M[i,j] = mu[i+j+shift]
    return mp.det(M)
def run(lam, z, N=8):
    mu = moments(lam, z, 2*N+4)
    D = [H(mu,n) for n in range(N+3)]
    Dall = [H(mu,n,1) for n in range(N+3)]
    Dlc = [H(mu,n,lastcol=True) if n>0 else mp.mpf(0) for n in range(N+3)]
    s = [Dlc[n]/D[n] for n in range(N+3)]
    a = {n: s[n+1]-s[n] for n in range(N+1)}       # x P_n = P_{n+1} + a_n P_n + b_n P_{n-1}
    alpha = {n: -1j*a[n] for n in a}                # a_n = i alpha_n
    beta = {n: D[n+1]*D[n-1]/D[n]**2 for n in range(1,N+1)}
    out = {"lam":str(lam),"zeta":mp.nstr(z,15),"rows":[]}
    for n in range(1,N):
        u = z*alpha[n] - (2*n+2*lam-1)
        rhs8 = z*Dall[n]/D[n] - (2*n+2*lam-1)
        proofform = z*(Dall[n+1]/D[n+1]-Dall[n]/D[n]) - (2*n+2*lam-1)
        out["rows"].append({"n":n,"alpha_imag_part":mp.nstr(mp.im(alpha[n]),5),
          "u_true":mp.nstr(u.real,12),"eq8_rhs":mp.nstr(rhs8,12),
          "proof_formula_all_shift":mp.nstr(proofform,12),
          "Dall_over_D":mp.nstr(Dall[n]/D[n],10),"D_n":mp.nstr(D[n],10)})
    # check recurrences (3),(4) for n>=1
    res3=[];res4=[]
    for n in range(1,N-2):
        al=lambda k: alpha[k].real; be=lambda k: beta[k].real
        c=2*n+1+2*lam
        r3 = al(n+1) - (mp.mpf(3)/(2*z)*c - al(n) + c/(2*z*be(n+1))*(be(n)-1+al(n)*((2*n-1+2*lam)/z - al(n))))
        r4 = be(n+2) - (be(n)+al(n+1)**2-al(n)**2+((al(n)*(2*n-1+2*lam)-al(n+1)*(2*n+3+2*lam))/z))
        res3.append(mp.nstr(r3,5)); res4.append(mp.nstr(r4,5))
    out["eq3_residuals"]=res3; out["eq4_residuals"]=res4
    out["beta_imag_max"]=mp.nstr(max(abs(mp.im(beta[n])) for n in beta),5)
    # Hirota (9) with tau_n = D_n(zeta): D^2 tau.tau = 2(tau tau'' - tau'^2) vs claimed coefficient
    hir=[]
    for n in range(1,4):
        f=lambda zz: H(moments(lam,zz,2*n+1),n)
        t=f(z); t1=mp.diff(f,z,1); t2=mp.diff(f,z,2)
        lhs=2*(t*t2-t1**2)
        Dn1=H(mu,n+1); Dm1=H(mu,n-1)
        hir.append({"n":n,"lhs":mp.nstr(lhs,10),"claimed_rhs":mp.nstr(2*n*(2*lam+2*n-1)/z**2*Dn1*Dm1,10),"toda_rhs_-2DD":mp.nstr(-2*Dn1*Dm1,10)})
    out["hirota"]=hir
    return out
res=[]
for lam,k in [(mp.mpf('1.25'),1),(mp.mpf(1),1),(mp.mpf('1.5'),1),(mp.mpf(2),1)]:
    z=mp.besseljzero(lam-1,k); res.append(run(lam,z))
# lambda=0: J_{-1}=-J_1 zero
res.append(run(mp.mpf(0), mp.besseljzero(1,1)))
print(json.dumps({"change_of_variables_exact": True, "points": res}, indent=1))
