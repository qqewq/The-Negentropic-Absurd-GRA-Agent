"""
Negentropic Generative Recursive Absurdity (GRA) Agent
======================================================
Reference implementation of iterative entropy‑reduction loop.
"""

import numpy as np
from scipy.special import softmax, rel_entr
from typing import Callable, List, Dict

class NegentropicGRAAgent:
    """
    Agent that starts with an absurd (high‑entropy) prior and
    iteratively applies a coherence cost and verification steps
    to produce a low‑entropy, practically useful distribution.
    """
    def __init__(self, idea_pool: List[str],
                 coherence_cost: Callable[[str], float],
                 verifier: Callable[[str], float] = None,
                 lambda_init: float = 1.0,
                 annealing: str = 'sqrt'):
        self.ideas = idea_pool
        self.N = len(idea_pool)
        self.coherence = coherence_cost
        self.verifier = verifier  # returns log P(D|idea)
        # uniform prior (max‑entropy)
        self.q = np.ones(self.N) / self.N
        self.lambda_init = lambda_init
        self.annealing = annealing
        self.step = 0

    def refine(self, steps: int = 1) -> None:
        """Apply the negentropic operator for a given number of steps."""
        for _ in range(steps):
            lam = self._lambda_schedule()
            costs = np.array([self.coherence(idea) for idea in self.ideas])
            # Boltzmann reweighting
            log_q_new = np.log(self.q + 1e-300) - lam * costs
            self.q = softmax(log_q_new)
            self.step += 1

    def verify(self, data: str = None) -> float:
        """
        Incorporate empirical verification.
        Returns information gain Delta I.
        """
        if self.verifier is None:
            return 0.0
        # compute log-likelihoods for each idea given data
        log_liks = np.array([self.verifier(idea) for idea in self.ideas])
        # prior entropy
        H_prior = -np.sum(rel_entr(self.q, self.q))  # just entropy
        H_prior = -np.sum(self.q * np.log(self.q + 1e-300))
        # posterior
        log_posterior_unnorm = np.log(self.q + 1e-300) + log_liks
        posterior = softmax(log_posterior_unnorm)
        H_post = -np.sum(posterior * np.log(posterior + 1e-300))
        self.q = posterior
        info_gain = H_prior - H_post
        return max(0.0, info_gain)

    def _lambda_schedule(self) -> float:
        if self.annealing == 'sqrt':
            return self.lambda_init / np.sqrt(1 + self.step)
        elif self.annealing == 'log':
            return self.lambda_init / np.log(2 + self.step)
        else:
            return self.lambda_init

    def get_best_idea(self) -> str:
        idx = np.argmax(self.q)
        return self.ideas[idx]

    def get_entropy(self) -> float:
        q_pos = self.q[self.q > 0]
        return -np.sum(q_pos * np.log(q_pos))

    def sample_idea(self, temperature=1.0) -> str:
        probs = softmax(np.log(self.q + 1e-300) / temperature)
        idx = np.random.choice(self.N, p=probs)
        return self.ideas[idx]


# Example coherence cost: penalise length, reward structure
def example_coherence(idea: str) -> float:
    return 0.1 * len(idea) - 0.05 * idea.count('e')  # dummy

# Example verifier (log-likelihood dummy)
def example_verifier(idea: str) -> float:
    return -abs(len(idea) - 10)  # prefer ideas of length ~10

if __name__ == "__main__":
    pool = ["silence remembers sound", "time travels backwards on Tuesdays",
            "gravity is a memory of falling", "light traps itself"]
    agent = NegentropicGRAAgent(pool, example_coherence, example_verifier)
    for i in range(10):
        agent.refine(1)
        info = agent.verify("experiment_1")
        print(f"Step {i}: entropy={agent.get_entropy():.3f}, info gain={info:.3f}, best='{agent.get_best_idea()}'")
