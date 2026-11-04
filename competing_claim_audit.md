# Competing 2026 claim: exact definitions and a reproducible inconsistency

Source: Johar M. Ashfaque, *On the Discrete Painlevé IV Structure of Oscillatory Gegenbauer Recurrence Coefficients*, dated 24 July 2026, six-page preprint hosted on ResearchGate.

URL: https://www.researchgate.net/publication/410769119_On_the_Discrete_Painleve_IV_Structure_of_Oscillatory_Gegenbauer_Recurrence_Coefficients

Accessed and read in full on 2 November 2026. The abstract and Proposition 3.1 claim that the symbolic formulas conjectured by Lyu–Zhou follow from a discrete-Painlevé and tau-function identification. This is an earlier public claim and should be disclosed when discussing priority. The following check concerns its displayed Proposition 3.1, not an assertion about all possible corrected versions of its approach.

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

The ResearchGate host refused automated access during the November 2026 revision, so this description of the preprint relies on the full reading recorded above. Readers should consult the original.
