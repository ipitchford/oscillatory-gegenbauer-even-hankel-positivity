# AI index: positivity and recurrence formulas for oscillatory Gegenbauer Hankel determinants (v0.2.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with
[README.md](README.md) and the paper [manuscript.pdf](manuscript.pdf) (LaTeX source [manuscript.tex](manuscript.tex)).
Version DOI 10.5281/zenodo.23941908 (0.2.0-candidate; 0.1.0-candidate was 10.5281/zenodo.23933929); concept DOI 10.5281/zenodo.23933928.

## Notation

mu_j^(alpha)(z) = integral_{-1}^{1} t^j (1-t^2)^alpha exp(i z t) dt, alpha > -1 real, z complex.
D_N^(alpha)(z) = det[mu_{i+j}^(alpha)(z)]_{i,j=0}^{N-1}, D_0 = 1. A monic orthogonal polynomial of degree N for the
complex weight exists (uniquely) iff D_N != 0. lambda = alpha + 1/2, u = z^2 in the polynomial sections.
mu_0 = sqrt(pi) Gamma(alpha+1) (2/z)^(alpha+1/2) J_(alpha+1/2)(z), and mu_j = i^(-j) d^j mu_0 / dz^j.
CDHI22 = Celsus, Deano, Huybrechs and Iserles (2022). MCM08 = Milovanovic, Cvetkovic and Marjanovic (2008).
LZ26 = Lyu and Zhou, arXiv:2607.19797v1. KR25 = Kounchev and Render, arXiv:2505.09964v1 (unrefereed).

## Claims and where they are proved

| ID | Claim | Location in [manuscript.tex](manuscript.tex) | Evidence type |
|---|---|---|---|
| C1 | D_{2r}^(alpha)(x) > 0 for all r >= 1, alpha > -1, real x (alpha = 0 is CDHI22 Theorem 4.3) | Theorem 1.1; Sections 2-4 | proof (continuation in alpha); numerical spot checks |
| C2 | Adjacent determinants D_N, D_{N+1} never vanish together; every complex zero of every D_N is simple | Lemma 2.1, Corollary 2.3 | proof (Pearson identity) |
| C3 | Large-frequency expansion of D_N with constants uniform on compact alpha intervals; even tail constant | Lemmas 3.1-3.2, Proposition 3.3, Corollary 3.4 | proof; tail constants checked numerically |
| C4 | Odd-size expansion; every odd-size determinant has infinitely many real zeros, located asymptotically | Proposition 3.5, Corollary 4.1 | proof |
| C5 | MCM08 Hankel polynomials: deg_u H_n = floor(n^2/4), generic deg_u V_n = n(n+1)/2, explicit leading coefficients; two exceptional parameter values lower the shifted degree | Theorems 5.1, 6.1 | proof; exact SymPy checks for small n |
| C6 | LZ26 Conjecture 2.5 (all four recurrence-coefficient formulas) in the stated ranges | Lemma 7.1, Theorem 7.2 | proof; residual checks |
| C7 | LZ26 Conjecture 2.7 (lambda = 0) in the stated ranges | Lemma 7.3, Theorem 7.4 | proof; reduced checks |
| C8 | Exact agreement with all 18 polynomials listed in LZ26 | Section 7.3 | exact comparison |
| C9 | Infinitely many irrational lambda > 1/2 admit a positive zero zeta of J_(lambda-1) with D_3 = 0 | Proposition 8.1 | proof |
| C10 | Exact Bessel-Jacobi determinant identity; even positivity for spherical-Bessel derivative determinants | Appendix A, Corollary 8.2 | proof |
| C11 | Critical length j_{7/2,1} for span{x^j cos x, x^j sin x : 0 <= j <= 3}, conditional on KR25 | Corollary 8.3 | proof, conditional on an unrefereed preprint |

## Prior claim

A ResearchGate preprint by J. M. Ashfaque dated 24 July 2026 (https://www.researchgate.net/publication/410769119)
claims the LZ26 recurrence formulas (C6, C7) via a discrete Painleve IV identification. Its change of variables is correct.
Its Proposition 3.1 fails as printed, at odd sizes (parity) and at even sizes, and no constant index shift or phase repairs it;
the difference formula in its proof is correct with the standard last-column shift. It gives no construction or degree
computation for the LZ26 polynomials ([competing_claim_audit.md](competing_claim_audit.md),
[prior_claim_check.py](prior_claim_check.py); manuscript Section 9). This release claims the first complete
proofs known to it of C6 and C7, not the first claim. The preprint does not state C1 or C5.

## Verification artefacts

- [verify.py](verify.py) -> [verification_results.json](verification_results.json): arbitrary-precision (mpmath 1.3.0)
  numerical and exact symbolic (SymPy 1.14.0) checks: independent moment formula, even determinants, Selberg values at
  the origin, alpha = 0 closed form, tail constants, Toda identity, formal degrees and leading coefficients, shifted
  numerators, Conjecture 2.5 residuals, Conjecture 2.7 reduced checks, exceptional specialisations, a symmetric-measure
  counterexample, the prior-claim formula check and a negative control. Checks raise explicitly (no assert), so
  `python -O` does not disable them. Run takes about one second.
  Scope: finite sizes and sample parameters only; all statements for all sizes rest on the written proofs.
- Pinned packages: [requirements.txt](requirements.txt). Replay: [README.md](README.md) "Reproduce"; CI:
  [.github/workflows/replay.yml](.github/workflows/replay.yml).

## Sources, novelty and review record

- [refs.bib](refs.bib) and [refs/crossref_records.jsonl](refs/crossref_records.jsonl): registry-identified bibliography
  and the Crossref and arXiv records it was copied from.
- [novelty_report.md](novelty_report.md): dated, bounded, formula-first prior-art audit.
- [competing_claim_audit.md](competing_claim_audit.md): exact checks of the earlier preprint.
- [target.yaml](target.yaml): machine-readable statements, fingerprints and open questions.
- [RESEARCH_GATES.json](RESEARCH_GATES.json): contribution map, sources read, limitation triage.
- [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md): internal AI-assisted review findings and what changed.
- Integrity: [MANIFEST.sha256](MANIFEST.sha256). Licences: [LICENSE.md](LICENSE.md) (text CC0-1.0, code MIT).
- Citation metadata: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or
proof-assistant formalisation. Existence only: no claim about distinct quadrature nodes, nonzero weights or numerical
conditioning. Odd degrees can fail. The general Carnicer-Mainar-Pena critical-length conjecture is open; C11 depends on
an unrefereed preprint. Priority holds only within a bounded search.
