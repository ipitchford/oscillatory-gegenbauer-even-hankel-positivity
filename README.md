# Positivity and recurrence formulas for oscillatory Gegenbauer Hankel determinants

Author: Anonymous. Text CC0-1.0; code MIT (see `LICENSE.md`). This is an unrefereed research candidate. Its review was internal and AI-assisted (see `REVIEW_SUMMARY.md`), not human peer review.

## In one paragraph

Some numerical methods for highly oscillatory integrals build Gaussian-type rules from polynomials that are orthogonal with respect to a *complex* weight, here \((1-t^2)^\alpha e^{ixt}\) on \([-1,1]\). Because the weight is complex, such a polynomial of degree \(N\) exists only when a Hankel determinant \(D_N^{(\alpha)}(x)\) is nonzero. This paper proves that **every even-size determinant is strictly positive, for every exponent \(\alpha>-1\) and every real frequency \(x\)**. So the even-degree polynomials always exist. Odd degrees can fail: every odd-size determinant has infinitely many real zeros.

## Main result

\[
D_{2r}^{(\alpha)}(x)>0,\qquad
D_N^{(\alpha)}(x)=\det\Big[\int_{-1}^{1}t^{i+j}(1-t^2)^\alpha e^{ixt}\,dt\Big]_{i,j=0}^{N-1},
\]
for all \(r\ge1\), \(\alpha>-1\), \(x\in\mathbb R\). The case \(\alpha=0\) is a theorem of Celsus, Deaño, Huybrechs and Iserles (2022). The extension to all \(\alpha\) uses continuation in \(\alpha\). A Pearson identity shows zeros are simple. A large-frequency expansion, with constants uniform in \(\alpha\), keeps zeros from arriving from infinity.

## Other results in the manuscript

- Every complex zero of every determinant is simple.
- Explicit even and odd large-frequency asymptotics, and the location of large odd-size zeros.
- Exact degrees and leading coefficients of the polynomial Hankel determinants of Milovanović, Cvetković and Marjanović (2008). These are the formal (generic) versions; two exceptional parameter values lower the shifted degree.
- Complete proofs of the recurrence-coefficient formulas in Conjectures 2.5 and 2.7 of Lyu and Zhou (2026), in their stated index ranges. They agree exactly with all 18 polynomials Lyu and Zhou list.
- An exact Bessel–Jacobi determinant identity. With a result of Kounchev and Render (an unrefereed preprint), it gives the critical length \(j_{7/2,1}\) for the space spanned by \(x^j\cos x, x^j\sin x\), \(0\le j\le3\).

## Prior claim (please read)

A ResearchGate preprint by J. M. Ashfaque, dated 24 July 2026, claims that the Lyu–Zhou recurrence formulas follow from a discrete Painlevé IV identification. It is therefore an earlier public claim on those two conjectures. Its key determinant formula (Proposition 3.1) fails as printed. `competing_claim_audit.md` gives exact checks, and the manuscript (Section 9) explains why no fixed index shift repairs it. This paper claims the first complete proofs *known to us* of those conjectures, not the first claim. As far as we have read, the preprint does not state the positivity theorem or the 2008 degree results.

## What is not proved

The general Carnicer–Mainar–Peña critical-length conjecture. And existence of an even-degree polynomial does not by itself give distinct quadrature nodes, nonzero weights or good conditioning.

## Files

| File | Contents |
| --- | --- |
| `manuscript.pdf`, `manuscript.tex` | The paper, with all proofs. |
| `verify.py` | Arbitrary-precision numerical and exact symbolic checks. Uses explicit checks that also run under `python -O`, and includes a negative control. |
| `verification_results.json` | Output of the final run. |
| `requirements.txt` | Pinned dependencies (mpmath 1.3.0, SymPy 1.14.0). |
| `novelty_report.md` | Formula-based prior-art audit. |
| `competing_claim_audit.md` | Exact check of the earlier claim. |
| `target.yaml` | Machine-readable statements, fingerprints and open questions. |
| `REVIEW_SUMMARY.md` | Review findings and what changed. |
| `AI_INDEX.md`, `RESEARCH_GATES.json`, `MANIFEST.sha256` | Package index, gate record, checksums. |
| `refs.bib`, `refs/crossref_records.jsonl` | The registry-identified bibliography as BibTeX and the Crossref and arXiv records it was copied from. |
| `CITATION.cff`, `.zenodo.json` | Citation and archive metadata. |
| `.github/workflows/replay.yml` | CI replay (with and without `-O`). |

## Reproduce

```bash
python -m pip install -r requirements.txt
python -O verify.py --output verification_results.json
```

The run takes about a second. The finite checks test formulas and conventions. **The proofs for all sizes are the arguments in the manuscript.**

## How to cite

Anonymous (2026). *Positivity and recurrence formulas for oscillatory Gegenbauer Hankel determinants*. Version 0.1.0-candidate. Evidence Press, unrefereed candidate. https://doi.org/10.5281/zenodo.23933929

- Version DOI: [10.5281/zenodo.23933929](https://doi.org/10.5281/zenodo.23933929); concept DOI (all versions): [10.5281/zenodo.23933928](https://doi.org/10.5281/zenodo.23933928)
- Repository: <https://github.com/ipitchford/oscillatory-gegenbauer-even-hankel-positivity>; release page: <https://evidencepress.org/releases/oscillatory-gegenbauer-even-hankel-positivity/>
