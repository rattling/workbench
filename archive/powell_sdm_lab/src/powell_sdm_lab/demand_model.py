"""
Online demand forecasting model

Tiny linear model with features: bias, sin(2πt/7), cos(2πt/7)
Updates via online SGD after observing each demand realization.
"""

import math


class OnlineDemandModel:
    """
    Linear demand forecaster with online learning.

    Model: ŷ = θ · φ(t)
    where φ(t) = [1, sin(2πt/7), cos(2πt/7)]

    Learning: Simple SGD update
    θ ← θ + α * (y - ŷ) * φ(t)
    """

    def __init__(self, learning_rate: float = 0.05):
        """
        Initialize model with zero weights.

        Args:
            learning_rate: Step size for SGD updates
        """
        self.theta = [80.0, 0.0, 0.0]  # Start near expected mean
        self.alpha = learning_rate

    def _features(self, t: int) -> list[float]:
        """Extract features for time t."""
        return [
            1.0,  # bias
            math.sin(2 * math.pi * t / 7),
            math.cos(2 * math.pi * t / 7),
        ]

    def predict(self, t: int) -> float:
        """
        Forecast demand for time t.

        Args:
            t: Time index

        Returns:
            Predicted demand
        """
        phi = self._features(t)
        return sum(w * f for w, f in zip(self.theta, phi))

    def update(self, t: int, y_obs: float) -> float:
        """
        Update model after observing true demand.

        Args:
            t: Time index
            y_obs: Observed demand

        Returns:
            Prediction error (y_obs - prediction)
        """
        phi = self._features(t)
        y_hat = self.predict(t)
        error = y_obs - y_hat

        # SGD update
        for i in range(len(self.theta)):
            self.theta[i] += self.alpha * error * phi[i]

        return error
