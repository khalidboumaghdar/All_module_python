from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class CardState(Enum):
    IN_HAND = "In Hand"
    PLAYED = "Played"
    DISCARDED = "Discarded"


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        if not isinstance(rarity, Rarity):
            raise ValueError("Rarity must be a Rarity enum member")
        self.name: str = name
        self.cost: int = cost
        self.rarity: Rarity = rarity
        self.state:  CardState = CardState.IN_HAND

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        pass

    def get_card_info(self) -> dict[str, Any]:
        return {
            'name':   self.name,
            'cost':   self.cost,
            'rarity': self.rarity.value,
            'state':  self.state.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
