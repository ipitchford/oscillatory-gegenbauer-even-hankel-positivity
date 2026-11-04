# Novelty audit: even oscillatory Gegenbauer Hankel determinants

Audit date: 2 November 2026. This is a bounded literature search, not proof that no prior theorem exists.

## Exact object

For real `alpha > -1`, let

\[
\mu_j^{(\alpha)}(\omega)=\int_{-1}^{1}t^j(1-t^2)^\alpha e^{i\omega t}\,dt,
\qquad
D_k^{(\alpha)}(\omega)=\det[\mu_{i+j}^{(\alpha)}(\omega)]_{i,j=0}^{k-1}.
\]

The proposed theorem is `D_(2r)^(alpha)(omega) > 0` for every integer `r >= 1`, every real `alpha > -1`, and every real frequency `omega`. Equivalently, every even-degree monic polynomial for the oscillatory Gegenbauer functional exists uniquely, at every real frequency.

The exact Bessel alias is

\[
\mu_0^{(\alpha)}(\omega)
=\sqrt\pi\,\Gamma(\alpha+1)
\left(\frac2\omega\right)^{\alpha+1/2}
J_{\alpha+1/2}(\omega),
\]

with its entire continuation at zero. Since `mu_j = i^(-j) d^j mu_0/domega^j`, the determinant is the signed consecutive-derivative Wronskian of this normalized Bessel function.

## Closest primary results inspected

### 1. Celsus, Deaño, Huybrechs, and Iserles (2022)

**The kissing polynomials and their Hankel determinants**, Transactions of Mathematics and Its Applications 6(1), tnab005.

- Publisher: https://academic.oup.com/imatrm/article/6/1/tnab005/6492355
- Preprint: https://arxiv.org/abs/1504.07297

The abstract and Section 4 explicitly prove existence of all even-degree kissing polynomials at every real frequency for the flat weight `exp(i omega x)`, namely the exact special case `alpha = 0`. Their even-degree existence proof uses imaginary-axis symmetry, the second-order differential equation, and control of escaping polynomial zeros. The paper also proves no common adjacent Hankel zeros and analyzes Hankel zeros, recurrence coefficients, and Painlevé V. Its discussion of Jacobi weights invokes Basor et al. for the Painlevé relation and Barhoumi et al. for asymptotics; the inspected material does not state the all-real-alpha even-degree existence theorem.

### 2. Milovanović, Cvetković, and Marjanović (2008)

**Orthogonal polynomials for the oscillatory-Gegenbauer weight**, Publications de l'Institut Mathématique, Nouvelle série 84(98), 49–60. DOI 10.2298/PIM0898049M.

- Author full text: https://www.researchgate.net/publication/235141000_Orthogonal_polynomials_for_the_oscillatory-Gegenbauer_weight

Theorem 2.2 proves existence at *all degrees*, under restrictions: their parameter `lambda = alpha + 1/2` is rational and greater than `-1/2`, and the nonzero frequency is a zero of `J_(lambda-1)`. The proof uses rational polynomial moments at such frequencies and transcendence of Bessel zeros of rational order. This does not imply an unrestricted-frequency even-degree theorem. Its all-degree conclusion is broader in parity and narrower in the allowed parameter-frequency pairs, so the two results should not be described as one wholly subsuming the other.

### 3. Lyu and Zhou (22 July 2026)

**Recurrence Coefficients of the Orthogonal Polynomials for Oscillatory Jacobi-type Weight Functions**, arXiv:2607.19797.

- Preprint record: https://arxiv.org/abs/2607.19797
- Author full text: https://www.researchgate.net/publication/410722516_Recurrence_Coefficients_of_the_Orthogonal_Polynomials_for_Oscillatory_Jacobi-type_Weight_Functions

The introduction and equation (1.1) retain precisely the rational-parameter and special-Bessel-zero frequency restrictions for the symmetric oscillatory Gegenbauer weight, explicitly imposed to ensure the orthogonal-polynomial sequence exists. The introduction credits the 2008 theorem. This is useful *current* evidence of the remaining general existence issue, but it does not itself state the proposed universal even-degree assertion as an open conjecture. No reference to Celsus was found in its searchable text.

### 4. Barhoumi (2021)

**Strong asymptotics of Jacobi-type kissing polynomials**, Integral Transforms and Special Functions 32(5–8), 377–394. DOI 10.1080/10652469.2021.1923707.

- Preprint: https://arxiv.org/abs/2101.04147
- Institutional full text: https://scholarworks.indianapolis.iu.edu/bitstreams/2e29b9df-779e-40f0-9be9-c016f69f51fd/download

This treats more general Jacobi-type weights and a varying-frequency limit `omega = lambda n`. Theorem 3.1 proves degree-exactly-n existence for *sufficiently large n* in the subcritical regime. Theorem 3.5 gives supercritical asymptotics along a specified subsequence `n in N(lambda, epsilon)`. These are asymptotic results, not all-finite-even-degree, all-frequency existence. This is a close subject-matter relation, not an exact collision.

### 5. Dimitrov and Xu (2019): exact-object near collision

**Wronskians of Fourier and Laplace transforms**, Transactions of the American Mathematical Society 372(6), 4107–4125. DOI 10.1090/tran/7809.

- Preprint: https://arxiv.org/abs/1606.05011
- Published author offprint: https://www.researchgate.net/publication/386702813_Wronskians_of_Fourier_and_Laplace_Transforms
- Author publications page: https://pages.uoregon.edu/yuan/pub.html

Corollary 2.13 (published p. 4115) proves that the signed derivative Wronskians of `x^(-lambda) J_lambda(x)`, for `lambda > -1/2`, are strictly *positive definite functions* on the real line, in every rank. The immediately preceding text explicitly distinguishes positive definiteness from pointwise positivity. Corollary 2.14 proves pointwise strict positivity only for rank 2. The proposed all-even theorem would strengthen this exact object to pointwise strict positivity in every even rank.

Theorem 4.1 gives a Wiener-tauberian equivalent: nonvanishing of a Wronskian is equivalent to density in `L^1(R)` of translates of the associated correlation kernel. An all-even nonvanishing theorem therefore has an immediate harmonic-analysis corollary. This is a routine corollary, not a separate independent breakthrough.

## CMP connection and scope

Carnicer, Mainar, and Peña, **Spherical Bessel functions and critical lengths**, DOI 10.1007/s13398-022-01365-8:

- https://link.springer.com/article/10.1007/s13398-022-01365-8
- https://zaguan.unizar.es/record/124006/files/texto_completo.pdf

Kounchev and Render, **On the critical length conjecture for spherical Bessel functions in CAGD**, 15 May 2025:

- https://arxiv.org/html/2505.09964v1
- https://arxiv.org/abs/2505.09964

The latter proves the rank-3 derivative-Hankel sign for all indices and consequently the CMP critical-length conjecture through index `n = 2`. Combined with the all-even positivity theorem and the exact Bessel–Jacobi identity in the manuscript appendix, this gives the new index `n = 3` case. Neither this case nor the general all-even theorem settles the full CMP conjecture. Higher odd ranks remain the obstruction.

## Search families

The searches included exact title and author searches; current 2025–2026 CMP searches; `oscillatory Gegenbauer` with `even`, `even-degree`, `existence`, and `all frequencies`; `Jacobi-type kissing` with `existence` and `even degree`; Bessel derivative Wronskians with `positive`, `positivity`, `nonvanishing`, `even order`, and `pointwise`; and Hankel determinant searches for Gegenbauer and Jacobi ensembles. Both available search engines were used. Near-collision checks included the 2019 Fourier-transform Wronskian paper, 2008 oscillatory Gegenbauer existence paper, 2021 Jacobi asymptotics, 2022 kissing-polynomial existence proof, and 2026 recurrence-coefficient paper.

## Calibrated conclusion

No exact all-real-parameter, all-frequency, every-even-rank pointwise positivity theorem was located. The mathematical result is a credible novelty candidate, with a clearly identified exact special case and exact-object weaker predecessor. No explicit published conjecture asserting the whole generalization was located. Thus describe it as a proposed solution to the general even-degree existence problem, subject to expert novelty verification, rather than as a certified solution of a named longstanding open conjecture. The full CMP conjecture remains open.

## Addendum: explicit degree and recurrence conjectures now targeted

The 2008 paper makes two explicit degree conjectures immediately below Table 1 on printed page 53. For its normalized moments `P_j(lambda,u)`, `u=zeta^2`, define `H_n=det[P_(i+j)]` and let `tilde H_n` replace the last column by the next moment column. The conjectured degrees are

\[
 \deg_uH_n=\lfloor n^2/4\rfloor,
 \qquad
 \deg_u(\widetilde H_nH_{n+1}-\widetilde H_{n+1}H_n)=n(n+1)/2.
\]

The source's prime on its shifted determinant is **not a parameter derivative** and is **not a shift of every matrix entry**. Exact object identification is essential here. Our proof of the first statement applies at every real `lambda>-1/2` and determines the leading coefficient. The second statement holds formally over `Q(lambda)`; the proof also identifies the two admissible specialized exceptions `(n,lambda)=(3,3/2)` and `(5,0)`, where the degree drops by one. These exceptions refine the natural generic reading of the source conjecture.

Lyu–Zhou (2026), Conjecture 2.5, makes stronger symbolic-form assertions for the recurrence coefficients, with normalized monic polynomials of specified degrees. Its Remark 2.6 explicitly restates the 2008 conjectural forms and adds leading coefficient predictions. Its Conjecture 2.7 gives the singular specialization `lambda=0` after removing powers of `u` from the determinants. The exact source ranges in Conjecture 2.7 are `alpha_(2k)` for `k>=3`; `alpha_(4j-1)` and `alpha_(4j+1)` for `j>=2`; and both beta formulas for `k>=1`. They intentionally omit the small alpha indices at which the same degree label would refer to two different monic polynomials.

The present derivations provide all-index proofs of these determinant degrees and symbolic forms. Complete consolidated proofs appear in Sections 5–7 of `manuscript.pdf` and `manuscript.tex`. The lambda-zero argument identifies the exact lowest coefficient with a Laguerre Gram determinant perturbed by a unit atom at zero; this yields the exact valuation `ord_(u=0)H_n=n-1`, not only a computed low-index pattern.

### Competing 2026 claims

- Johar M. Ashfaque, **On the Discrete Painlevé IV Structure of Oscillatory Gegenbauer Recurrence Coefficients**, ResearchGate posting dated 24 July 2026, https://www.researchgate.net/publication/410769119_On_the_Discrete_Painleve_IV_Structure_of_Oscillatory_Gegenbauer_Recurrence_Coefficients . This purports to explain the recurrence patterns through Painlevé structure. Its Proposition 3.1 contains a concrete incorrect determinant formula: the claimed all-entry-shifted ratio at size 1 equals `2i lambda/zeta` at the special Bessel frequencies and does not give the stated real recurrence quantity. A separately documented audit is in `competing_claim_audit.md`. We therefore located a competing claim, but not a verified proof. This must remain disclosed; it would be inaccurate to say that no proof has ever been claimed.
- **Ideosphere, oscillatory Gegenbauer recurrence project**, https://ideosphere.ai/papers/oscjacobi-rec , public entry dated 7 September 2026. This explicitly reports finite symbolic certification of the recurrence formulas through alpha index 12, beta index 13, and the determinant degree pattern through size 16. Its stated scope is finite verification and does not establish an all-index theorem. This is useful current status evidence, but it is not treated as an independent primary proof of the general assertions.

## Addendum: formula-level alias audit

The final bounded search used the exact polynomial determinant, oscillatory Gegenbauer, Lommel polynomials, Umemura polynomials, Bessel tau determinants, and the current paper's identifier. It did not locate an all-index theorem equivalent to the normalized `H_n` degree and recurrence assertions. The following near matches were inspected at formula level.

### Karlin–Szegő and order-shifted Bessel determinants

The classical even Hankel derivative sign theorem applies to `g_nu(u)=u^(-nu/2)J_nu(2 sqrt(u))`, whose derivatives shift the Bessel order. The oscillatory Gegenbauer problem instead differentiates `omega^(-nu)J_nu(omega)` with respect to `omega`. A nonlinear variable change does not preserve a consecutive-derivative Hankel determinant up to a scalar factor. Already in rank 2,

\[
 H_2[f\circ\phi]
 =\phi'^2\bigl(ff''-f'^2\bigr)\circ\phi
   +\phi''(ff')\circ\phi.
\]

Thus classical order-shifted Bessel inequalities are not an automatic proof of our all-even statement. The independently inspected account is arXiv:1101.4624, Section 2.2, https://arxiv.org/abs/1101.4624 . No bridge establishing an exact implication was located.

### Lommel polynomials and Rayleigh-sum Hankel determinants

Árpád Baricz, **Hankel determinant of the Rayleigh sums of zeros of Bessel functions**, arXiv:1708.07729v1, Theorem 1, https://arxiv.org/abs/1708.07729v1 and author full text https://www.researchgate.net/publication/319312045_Hankel_determinant_of_the_Rayleigh_sums_of_zeros_of_Bessel_functions .

Its Hankel entries are `sigma_k(nu)=sum_m j_(nu,m)^(-2k)`. The theorem evaluates this determinant as a product in the order parameter, using Lommel orthogonality. These are sums over reciprocal Bessel zeros, not polynomial moments obtained by evaluating a Bessel transform at one special zero. There is no frequency variable `u` in this determinant. The retrieved formula therefore is a different object and does not give the target polynomial degree theorem.

### Umemura polynomials

Peter A. Clarkson, Chun-Kong Law and Chia-Hua Lin, **A Constructive Proof for the Umemura Polynomials of the Third Painlevé Equation**, SIGMA 19 (2023), 080, DOI 10.3842/SIGMA.2023.080; primary PDF https://sigma-journal.com/2023/080/sigma23-080.pdf .

Theorem 2.3 and Remarks 2.4 define the monic Umemura sequence by a differential-difference recurrence and give degree `n(n+1)/2`. Its initial values and recurrence differ from the normalized moment determinants here. The paper's determinant construction uses Schur/Laguerre-type entries. The presence of a quadratic degree pattern and a Hankel or Wronskian representation is insufficient to identify these families. No parameter or variable substitution equating our `H_n` to those polynomials was found.

### Bessel tau functions: Euler derivatives are different

Peter A. Clarkson, **Classical solutions of the degenerate fifth Painlevé equation**, J. Phys. A: Math. Theor. 56 (2023), 134002, DOI 10.1088/1751-8121/acbef1; primary full text https://www.researchgate.net/publication/368807575_Classical_solutions_of_the_degenerate_fifth_Painleve_equation .

Theorem 3.6 and equations (30), (47) use the determinant

\[
 \tau_n(x)=\det[(x\partial_x)^{i+j}\phi_\mu(x)]_{i,j=0}^{n-1},
\]

where `phi_mu` is a Bessel solution. These Euler derivatives are not the ordinary derivatives in the oscillatory Gegenbauer determinant. A concrete diagnostic rules out the naive identification even at the special frequencies. Take `lambda=0`, `f=J_0`, and `zeta` a positive zero of `J_1`. The Bessel equation gives

\[
 \det[(x\partial_x)^{i+j}J_0(x)]_{i,j=0}^{2}\big|_{x=\zeta}=0,
 \qquad
 \det[J_0^{(i+j)}(\zeta)]_{i,j=0}^{2}
       =2J_0(\zeta)^3/\zeta^2\ne0.
\]

Thus the two determinants cannot coincide there up to a nonvanishing scalar prefactor. This does not rule out all deeper integrable transformations, but it prevents a false direct prior-art identification.

Yu Chen, Shuai-Xia Xu and Yu-Qiu Zhao, **Asymptotics of the determinant of the modified Bessel functions and the second Painlevé equation**, arXiv:2402.11233, https://arxiv.org/abs/2402.11233 , instead uses a Toeplitz matrix with entries `I_(i-j-nu)` and identifies its Painlevé III tau structure. This is again a different derivative/order structure. No direct implication for our `H_n` degree or special-frequency recurrence conjectures was established.

## Addendum: rationality is substantive

Section 8 of the manuscript proves that for every integer `m>=2` there exists an irrational `lambda_m>1/2` such that, at `zeta_m=j_(lambda_m-1,m)`, the rank-3 moment determinant vanishes. The proof combines the exact quadratic `H_3` with continuity of Bessel zeros in order and the fixed-index asymptotic `j_(nu,m)/nu -> 1`; DLMF 10.21.32 records the expansion, https://dlmf.nist.gov/10.21.E32 . Infinitely many distinct parameters occur. Thus the 2008 theorem cannot simply be extended from rational to all real parameters while retaining all degrees. This refutes a natural extension, not an explicitly located published conjecture. It is compatible with our universal even-degree theorem.

## Final audit assessment

The literature record now supports a precise claim stronger than the initial existence proposal: the work supplies candidate complete proofs of explicitly stated 2008 determinant-degree conjectures and 2026 symbolic recurrence conjectures, including the nontrivial lambda-zero specialization. The current universal even-degree theorem is a separate credible extension of Celsus et al. The inspected evidence does not establish a theorem-level collision, but it does reveal one flawed competing proof claim and one finite verification project. Expert novelty review remains needed. The full CMP critical-length conjecture remains unresolved.


## Frozen-deliverable status

The consolidated manuscript contains complete proofs of both 2026 conjectures in their stated ranges. An internal AI-assisted review found no unresolved core proof gap; it is not independent external peer review. Historical priority remains bounded by the searches and competing-claim examination recorded above.
