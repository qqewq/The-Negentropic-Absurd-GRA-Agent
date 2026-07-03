# Derivations

## A. Convergence of iterative refinement
Let \(Q_0\) be a high‑entropy initial distribution. Define

\[
Q_{t+1}(x) = \frac{Q_t(x) e^{-\lambda \mathcal{C}(x)}}{Z_t},\qquad Z_t = \sum_x Q_t(x) e^{-\lambda \mathcal{C}(x)}.
\]

### Lemma 1 – Monotonic free energy decrease
Define the free energy \(F_t = \mathbb{E}_{Q_t}[\mathcal{C}] - \frac{1}{\lambda} S(Q_t)\). Then

\[
F_{t+1} \le F_t,
\]

with equality iff \(Q_t\) is already a Gibbs distribution for \(\mathcal{C}\).

*Proof.* The KL divergence \(D_{KL}(Q_{t+1} \| Q_t)\) is non‑negative, giving the inequality after rearranging the log‑partition ratio.

### Theorem 1 – Entropy bound
If \(\mathcal{C}_{\min} \le \mathcal{C}(x) \le \mathcal{C}_{\max}\), then

\[
S(Q_T) \ge S(Q_0) - \lambda T (\mathcal{C}_{\max} - \mathcal{C}_{\min})^2.
\]

Thus with appropriately decaying \(\lambda_t = 1/\sqrt{t}\) we guarantee convergence to a stationary point.

## B. Information gain from verification
After an experiment yielding data \(D\), the posterior is

\[
Q_{\text{post}}(x) = \frac{Q_{\text{prior}}(x) P(D|x)}{P(D)}.
\]

The **information gain** (reduction of uncertainty) is

\[
\Delta I = S(Q_{\text{prior}}) - S(Q_{\text{post}}) = \mathbb{E}_{Q_{\text{post}}}[\log P(D|x)] - \log P(D) \ge 0.
\]

When \(D\) strongly confirms some subset of ideas, \(\Delta I\) is large – i.e., **absurdity is transformed into verified knowledge**.

## C. Rate‑distortion analogy
The whole process can be seen as a rate‑distortion problem where the distortion is the coherence cost \(\mathcal{C}\). The minimal achievable entropy for a given expected distortion \(D\) is

\[
R(D) = \min_{Q: \mathbb{E}_Q[\mathcal{C}] \le D} S(Q).
\]

Our iterative scheme approximates the \(R(D)\) curve, allowing to trade off remaining “absurdity” against practical fidelity.
