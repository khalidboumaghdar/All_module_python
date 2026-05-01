from abc import ABC, abstractmethod
from enum import Enum


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    MAGIC = "magic"


class Combatable(ABC):

    @abstractmethod
    def attack(self, target: list) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
