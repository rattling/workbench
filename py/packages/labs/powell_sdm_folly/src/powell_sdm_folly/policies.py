"""
Decision policies

Two contrasting approaches:
- Policy A: Fixed base-stock (no learning)
- Policy B: Forecast-driven base-stock (with online demand model)
"""

from powell_sdm_folly.demand_model import OnlineDemandModel


class PolicyA:
    """
    Constant base-stock policy.

    Decision: q_t = max(0, S - inventory)

    No learning, no model. Represents naive approach.
    """

    def __init__(self, target_stock: float):
        """
        Initialize policy.

        Args:
            target_stock: Fixed base-stock level S
        """
        self.S = target_stock

    def decide(self, inventory: float, t: int) -> float:
        """
        Compute order quantity.

        Args:
            inventory: Current inventory level
            t: Time index (unused by this policy)

        Returns:
            Order quantity
        """
        return max(0, self.S - inventory)

    def learn(self, t: int, demand: float):
        """No learning in this policy."""
        pass

    def get_forecast(self, t: int) -> float | None:
        """No forecast available."""
        return None

    def get_forecast_error(self, t: int, demand: float) -> float | None:
        """No forecast error to report."""
        return None


class PolicyB:
    """
    Forecast-driven base-stock policy with online learning.

    Decision: q_t = max(0, ŷ_t + safety - inventory)
    where ŷ_t is the demand forecast

    Embeds demand model directly in decision loop.
    """

    def __init__(self, safety_stock: float, learning_rate: float = 0.05):
        """
        Initialize policy with demand model.

        Args:
            safety_stock: Safety buffer above forecast
            learning_rate: Learning rate for demand model
        """
        self.safety = safety_stock
        self.model = OnlineDemandModel(learning_rate=learning_rate)
        self._last_forecast = None

    def decide(self, inventory: float, t: int) -> float:
        """
        Compute order quantity using forecast.

        Args:
            inventory: Current inventory level
            t: Time index

        Returns:
            Order quantity
        """
        forecast = self.model.predict(t)
        self._last_forecast = forecast

        target = forecast + self.safety
        return max(0, target - inventory)

    def learn(self, t: int, demand: float):
        """
        Update demand model after observing realized demand.

        Args:
            t: Time index
            demand: Observed demand
        """
        self.model.update(t, demand)

    def get_forecast(self, t: int) -> float | None:
        """Get last forecast (for tracing)."""
        return self._last_forecast

    def get_forecast_error(self, t: int, demand: float) -> float | None:
        """Compute forecast error (for tracing)."""
        if self._last_forecast is None:
            return None
        return demand - self._last_forecast
