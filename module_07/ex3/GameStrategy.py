from abc import ABC, abstractmethod
from enum import Enum


class StrategyName(Enum):
    AGGRESSIVE = "AggressiveStrategy"
    DEFENSIVE = "DefensiveStrategy"
    BALANCED = "BalancedStrategy"


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> StrategyName:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
