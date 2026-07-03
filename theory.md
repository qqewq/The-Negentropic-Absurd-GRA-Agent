# Theory: Entropic Absurdity and Negentropic Refinement

## 1. Absurdity as an information source
An **absurd statement** is one whose internal probability under current knowledge is extremely low.  
We model the space of all conceivable statements \(\Omega\) with a background measure \(\mu\).  
For a statement \(x\), the **surprisal** is \(-\log p(x)\).  
**Absurdity entropy** of a distribution \(Q\) over ideas is

\[
S_{\text{abs}}(Q) = -\sum_{x} Q(x) \log Q(x) + \beta \, \mathbb{E}_Q[-\log p(x)]
\]

where \(\beta\) balances intrinsic randomness and contextual implausibility.  
A high \(S_{\text{abs}}\) corresponds to a generator that produces varied, highly unexpected outputs – the raw GRA.

## 2. Negentropic operator \(\mathcal{N}\)
We introduce a **negentropic operator** \(\mathcal{N}_\lambda\) that acts on a distribution \(Q_t\) at step \(t\):

\[
Q_{t+1}(x) = \frac{1}{Z_t} Q_t(x) \, e^{-\lambda \mathcal{C}(x)}
\]

\(\mathcal{C}(x)\) is a **coherence cost** derived from logical consistency, empirical adequacy, and aesthetic harmony.  
\(\lambda > 0\) controls the strictness of refinement. \(Z_t\) normalises.

This is equivalent to a Boltzmann‑type selection that exponentially suppresses incoherent ideas.

## 3. Entropy evolution
The entropy of the distribution evolves as

\[
S(Q_{t+1}) = S(Q_t) - \lambda \, \text{Cov}_{Q_t}(\mathcal{C}, -\log Q_t) + \lambda^2 \text{Var}_{Q_t}(\mathcal{C}) + o(\lambda^2)
\]

If \(\mathcal{C}\) is chosen such that it correlates positively with the information content needed for practical utility, then \(S\) decreases monotonically.

## 4. Iterative practical extraction
After \(T\) iterations, we sample from the low‑entropy distribution \(Q_T\).  
The resulting artefacts are **negentropic applications**: theories with high predictive power, efficient machines, compelling art.

The total **negentropy gain** is

\[
\Delta N = S_{\text{abs}}(Q_0) - S(Q_T) = \text{information converted into structured knowledge}.
\]

## 5. Verification condition
A refinement step is **verified** when empirical data \(D\) satisfies

\[
P(D | x, \text{background}) \gg P(D | \text{null model}).
\]

Verification further reduces entropy by conditioning: \(Q_{t+1} \propto Q_t \cdot P(D|x)\).  
This closes the loop between absurd generation and practical truth.
