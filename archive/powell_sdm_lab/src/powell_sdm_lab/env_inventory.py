"""
Inventory environment

Encodes system dynamics and cost structure.
Implements the state transition: S_t → x_t → S^x_t → W → S_{t+1}
"""

from dataclasses import dataclass


@dataclass
class StepRecord:
    """Complete record of one time step through Powell's loop."""

    t: int
    inventory_pre: float
    order_qty: float
    inventory_post: float
    demand: float
    sales: float
    inventory_next: float
    stockout: float
    cost: float


class InventoryEnv:
    """
    Single-product inventory system.

    Dynamics:
        - Order arrives immediately
        - Demand is realized
        - Sales = min(inventory_post, demand)
        - Leftover inventory carries forward

    Costs:
        - Ordering: c * order_qty
        - Holding: h * inventory_next
        - Penalty: p * stockout
    """

    def __init__(
        self,
        initial_inventory: float,
        ordering_cost: float = 0.2,
        holding_cost: float = 0.05,
        penalty_cost: float = 1.0,
    ):
        """
        Initialize environment.

        Args:
            initial_inventory: Starting inventory level
            ordering_cost: Per-unit ordering cost
            holding_cost: Per-unit holding cost per period
            penalty_cost: Per-unit stockout penalty
        """
        self.inventory = initial_inventory
        self.t = 0

        self.c = ordering_cost
        self.h = holding_cost
        self.p = penalty_cost

    def step(self, order_qty: float, demand: float) -> StepRecord:
        """
        Execute one time step of the inventory system.

        Powell's loop:
            S_t (pre-decision) → x_t (decision) → S^x_t (post-decision)
            → W_{t+1} (exogenous) → S_{t+1} (next state)

        Args:
            order_qty: Decision (how much to order)
            demand: Exogenous information (realized demand)

        Returns:
            Complete record of the step
        """
        # Pre-decision state
        inventory_pre = self.inventory

        # Post-decision state (after ordering)
        inventory_post = inventory_pre + order_qty

        # Transition (after demand realization)
        sales = min(inventory_post, demand)
        stockout = max(0, demand - inventory_post)
        inventory_next = inventory_post - sales

        # Cost calculation
        cost = self.c * order_qty + self.h * inventory_next + self.p * stockout

        # Update state
        self.inventory = inventory_next
        self.t += 1

        return StepRecord(
            t=self.t - 1,  # Record the time we just completed
            inventory_pre=inventory_pre,
            order_qty=order_qty,
            inventory_post=inventory_post,
            demand=demand,
            sales=sales,
            inventory_next=inventory_next,
            stockout=stockout,
            cost=cost,
        )

    def reset(self, initial_inventory: float):
        """Reset environment to initial state."""
        self.inventory = initial_inventory
        self.t = 0
