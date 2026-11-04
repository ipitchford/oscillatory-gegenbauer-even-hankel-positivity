# Competing 2026 claim: exact definitions and a reproducible inconsistency

Source: Johar M. Ashfaque, *On the Discrete Painlevé IV Structure of Oscillatory Gegenbauer Recurrence Coefficients*, dated 24 July 2026, six-page preprint hosted on ResearchGate.

URL: https://www.researchgate.net/publication/410769119_On_the_Discrete_Painleve_IV_Structure_of_Oscillatory_Gegenbauer_Recurrence_Coefficients

Read in full (six pages) on 2 November 2026, and again from the complete text for version 0.2.0 on 4 November 2026. Its abstract says the forms conjectured by Lyu–Zhou arise as rational solutions of a discrete Painlevé IV system, and the end of its Section 3 states that identifying its tau-functions with the Lyu–Zhou polynomials establishes those formulas. This is an earlier public claim and should be disclosed when discussing priority. The following check concerns its displayed Proposition 3.1, not an assertion about all possible corrected versions of its approach.

## Relevant definitions as mathematical formulas

The weight is \(w(x)=(1-x^2)^{\lambda-1/2}e^{i\zeta x}\), with \(\lambda>-1/2\) and \(J_{\lambda-1}(\zeta)=0\). The polynomial recurrence is

\[
 xP_n=P_{n+1}+i\alpha_nP_n+\beta_nP_{n-1}.
\]

Definition 2.1, equation (5), sets

\[
 u_n=\zeta\alpha_n-(2n+2\lambda-1),
 \qquad v_n=\zeta^2\beta_n.
\]

Proposition 3.1 defines

\[
 \mu_k=\int_{-1}^1x^kw(x)\,dx,
 \quad D_n=\det[\mu_{i+j}]_{i,j=0}^{n-1},
 \quad D_n^{(1)}=\det[\mu_{i+j+1}]_{i,j=0}^{n-1}.
\]

Its equation (8) then claims

\[
 u_n=\zeta\frac{D_n^{(1)}}{D_n}-(2n+2\lambda-1).
 \tag{A}
\]

The determinant \(D_n^{(1)}\) here shifts **every** moment index by one. It is not the single last-column shift that gives the subleading coefficient of a monic orthogonal polynomial.

## Exact countercheck

Take \(\lambda=0\), and let \(\zeta>0\) be any zero of \(J_{-1}=-J_1\). Then

\[
 \mu_0=\pi J_0(\zeta)\ne0,
 \qquad \mu_1=i\pi J_1(\zeta)=0.
\]

At \(n=1\), equation (A) therefore gives \(u_1=-1\).

But Lyu–Zhou's exact initial value, used as an input by the preprint, is

\[
 \alpha_1=\frac{2(\lambda+1)}\zeta
 -\frac{\zeta(2\lambda+1)}{\zeta^2-2\lambda}.
\]

At \(\lambda=0\), this is \(\alpha_1=1/\zeta\). Definition 2.1 therefore gives \(u_1=0\), contradicting (A).

This discrepancy can be checked without any asymptotics, numerical Bessel evaluation or geometric classification. Thus Proposition 3.1 cannot prove the claimed normalisation as written. A different argument or a corrected statement might still be possible; this audit makes no judgement about such an unpublished repair.

## Permitted conclusion

The present degree proof should be described as an all-rank proof with a bounded literature audit. It should disclose that a previous public preprint claimed a wider result and that the displayed formula supporting that claim fails this exact check. A claim of historical priority is not justified merely by detecting this gap.

## Addendum (4 November 2026): a parity check that rules out simple repairs

For real \(\zeta\), \(\overline{\mu_j}=(-1)^j\mu_j\). Hence \(\overline{D_n^{(1)}}=(-1)^{n^2}D_n^{(1)}=(-1)^nD_n^{(1)}\): the all-entry-shifted determinant is purely imaginary for odd \(n\) and real for even \(n\), while \(D_n\) is real. At every nonzero real zero \(\zeta\) of \(J_{\lambda-1}\), the Bessel recurrence gives \(\zeta\mu_1/\mu_0=2i\lambda\), so the right side of (A) at \(n=1\) is \(2i\lambda-(2\lambda+1)\), not real when \(\lambda\neq0\). Because the right side alternates between imaginary and real with the parity of \(n\), no fixed index shift or constant phase repairs (A) for all \(n\). `verify.py` checks the ratio and the parity numerically (section `prior_claim_formula_check`).

## Addendum (4 November 2026, version 0.2.0): what the preprint gets right, and what else fails

Checks are in `prior_claim_check.py` (output `prior_claim_check.json`).

Correct, and credited:

- Its equations (3)-(4), the Lyu–Zhou difference equations for \(\alpha_n,\beta_n\), hold: residuals below \(10^{-38}\) at \((\lambda,\zeta)=(5/4,j_{1/4,1}),(1,j_{0,1}),(3/2,\pi),(2,j_{1,1})\), and below \(10^{-22}\) at \(\lambda=0\), \(\zeta=j_{1,1}\) (quadrature-limited).
- The change of variables in its Theorem 2.2 is exactly right: SymPy reduces (6) and (7) to identities.
- The \(v_n\) half of (8) is the standard \(\beta_n=D_{n+1}D_{n-1}/D_n^2\).
- Its proof of Proposition 3.1 writes \(\alpha_n=D^{(1)}_{n+1}/D_{n+1}-D^{(1)}_n/D_n\). With \(D^{(1)}_n\) taken as the single last-column shift and a factor \(-i\), that is the standard correct formula; the check computes \(\alpha_n\) this way, and the results satisfy (3)-(4) to the precision above. The failure is in the displayed statement (A), which uses a single ratio with every index shifted.

Further failures:

- (A) fails at even \(n\) too, where both sides are real: at \(\lambda=5/4\), \(n=2\), the right side is \(-6.7778\) and the true \(u_2\) is \(-5.4311\).
- Its bilinear equation (9), read with \(\tau_n=D_n\), fails: the left side equals \(-2\tau_{n+1}\tau_{n-1}\) (the Toda identity, to 10 digits for \(n=1,2,3\)), not \(2n(2\lambda+2n-1)\zeta^{-2}\tau_{n+1}\tau_{n-1}\). The preprint leaves the normalisation of \(\tau_n\) unspecified, so only this natural reading is checked.
- \(D_n\) is a Bessel-function expression in \(\zeta\), not a polynomial in \(\zeta^2\). The identification of \(\tau_n\) with the Lyu–Zhou \(X_n\) is asserted without a construction or degree computation, which is what Conjectures 2.5 and 2.7 require. So even a corrected Proposition 3.1 would not prove them.

Not claimed by the preprint: positivity of even-size Hankel determinants (it says only that the determinants "admit real zeros", which for even sizes is ruled out by Theorem 1.1), or the 2008 degree results of Milovanović, Cvetković and Marjanović. Its Sections 4 (oscillatory Jacobi weights) and 5 (continuum limit) are sketches that this release does not use and did not assess.

Correction to version 0.1.0: that version called the failure "not an index slip" and gave the last-column-shift difference formula as our own remark, without noting that the preprint's proof already writes it. It also did not credit the correct parts listed above.

