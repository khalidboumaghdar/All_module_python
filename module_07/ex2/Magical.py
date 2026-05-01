from abc import ABC, abstractmethod
from enum import Enum


class MagicType(Enum):
    ARCANE = "arcane"
    FIRE = "fire"
    ICE = "ice"
    SHADOW = "shadow"


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
