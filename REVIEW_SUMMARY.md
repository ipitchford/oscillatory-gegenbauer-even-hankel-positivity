# Review record (public, AI-assisted)

**What this is.** Before release the manuscript went through an internal, AI-assisted review in November 2026: five reviewer roles (editor, methodology, domain, perspective, devil's advocate) run as AI agents, a separate AI adversarial review, a clean replay of `verify.py` (normal and `python -O`), one revision round, a re-review and a targeted audit of every rewritten proof. **None of this is human peer review or independent reproduction.**

## Findings and what changed

| Finding | Severity | Resolution |
| --- | --- | --- |
| The large-frequency expansion, uniform in the exponent, on which the main theorem rests, was only sketched (multivariable Taylor remainders, mixed corner terms). | Major | Rewritten. New Lemma "uniform endpoint lemma" proves the one-variable expansion with constants uniform on compact exponent intervals; a moment-splitting lemma and an exact polynomial reduction show the determinant is a finite sum of products of such one-variable integrals, so no multivariable remainder occurs. The derivative expansion and joint continuity are proved separately. Audited afterwards: no open issue. |
| The earlier ResearchGate claim (Ashfaque, July 2026) was disclosed too briefly, and the rebuttal could be read as an index slip. | Major | The prior claim is now stated in the introduction and abstract: it claims the Lyu–Zhou recurrence formulas. The paper claims the first complete proofs known to it, not the first claim. A parity argument shows the printed formula fails for every odd size and cannot be fixed by a constant index shift or phase. |
| Lyu–Zhou's conjectures posit only unspecified monic polynomials. | Major | The paper says what is actually proved, and a new table shows exact agreement with all 18 polynomials Lyu and Zhou list. |
| The base case quoted from Celsus et al. needed its exact scope. | Major | Quoted: unconditional, every real frequency, flat weight. |
| The n = 3 critical-length corollary depends on an unrefereed preprint (Kounchev–Render). | Major | Now flagged as conditional in the abstract, introduction and proof. |
| Significance and the numerical context were under-argued; no roadmap. | Minor | Added a plain-language paragraph, a roadmap and quadrature references. The existence-only limit (no claim about distinct nodes or conditioning) is stated. |
| `verify.py` relied on `assert`, which `python -O` removes. | Minor | Replaced by explicit checks; added a prior-claim formula check and a negative control. |
| A divisibility step in the λ = 0 valuation lemma was implicit. | Minor | Added. |

## Not done (considered extensions)

Distinct quadrature nodes with nonzero weights, interlacing of odd-size zeros, critical lengths for n ≥ 4, and an independent certificate replacing the Kounchev–Render input were considered. None was tractable within this revision, and none is claimed.
