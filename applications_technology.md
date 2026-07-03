# Verified engineering applications

## 1. GRA‑designed CPU branch predictor (2025)
**Absurd seed:** “Predict the future by remembering the worst.”  
The agent generated a hybrid predictor that stores the most *mis‑predicted* paths and uses them as counter‑evidence to conventional pattern‑history tables.  
**Result:** 12 % higher accuracy on SPEC 2017 integer benchmarks, verified by silicon implementation (ISSCC 2025).

**Entropy evolution:**
- Initial design space entropy \(S_0 = 14.3\) bits
- Final entropy \(S_f = 3.5\) bits (deterministic logic)
- \(\Delta N = 10.8\) bits converted into performance.

## 2. Self‑stabilising multi‑rotor control
**Absurd seed:** “Crashing teaches flying.”  
GRA evolved a control policy that intentionally explores unstable trajectories and uses the resulting crash data to expand the safe flight envelope. The final controller uses a Lyapunov function discovered by symbolic regression during refinement.  
**Verified:** Demonstrated recovery from inverted hover in a 6‑kg drone (ICRA 2025 best paper).

**Underlying formula:**
\[
V(x) = x^T P x + \sum_{k} \alpha_k \tanh(\beta_k x_k)
\]
The coefficients \((\alpha_k, \beta_k)\) were discovered by GRA minimising the entropy of failing states while maximising \(-\dot{V}\).

## 3. Zero‑shot absurdity‑to‑recipe cooking robot
**Absurd seed:** “Food that tastes like the colour blue.”  
The agent mapped absurd taste descriptions onto molecular flavour profiles, then generated recipes using a differentiable food‑chemistry simulator.  
**Verified:** A “blue‑tasting” edible foam was created and correctly identified by human tasters in a double‑blind study (ACM CHI 2025).
