from abc import ABC, abstractmethod
from enum import Enum
from ex0.Card import Card


class CreatureType(Enum):
    DRAGON = "dragon"
    GOBLIN = "goblin"


class SpellType(Enum):
    FIREBALL = "fireball"
    LIGHTNING_BOLT = "lightning_bolt"


class ArtifactType(Enum):
    MANA_RING = "mana_ring"
    MANA_CRYSTAL = "mana_crystal"


class CardFactory(ABC):

    @abstractmethod
    def create_creature(
        self,
        name_or_power: CreatureType | None = None
    ) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: SpellType | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: ArtifactType | None = None
    ) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
