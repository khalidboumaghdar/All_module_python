from enum import Enum
from typing import Any
from ex0.Card import Card, Rarity, CardState


class ArtifactEffect(Enum):
    HEAL = "Heal all friendly creatures"
    BOOST = "Boost attack of all creatures"
    SHIELD = "Shield all friendly creatures"
    DESTROY = "Destroy target creature"


class ArtifactState(Enum):
    INACTIVE = "Inactive"
    ACTIVE = "Active"
    DESTROYED = "Destroyed"


class ArtifactCard(Card):

    def __init__(
            self,
            name:       str,
            cost:       int,
            rarity:     Rarity,
            age_effect: int,
            effect:     ArtifactEffect,
    ) -> None:
        if not isinstance(effect, ArtifactEffect):
            raise ValueError("Effect must be an ArtifactEffect enum member")
        if not isinstance(age_effect, int) or age_effect < 0:
            raise ValueError("Age effect must be a non-negative integer")
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.age_effect: int = age_effect
        self.effect: ArtifactEffect = effect
        self.is_play: bool = False
        self.artifact_state: ArtifactState = ArtifactState.INACTIVE

    def get_card_info(self) -> dict[str, Any]:
        info: dict = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.age_effect
        info['effect'] = self.effect.value
        info['artifact_state'] = self.artifact_state.value
        return info

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        self.is_play = True
        self.state = CardState.PLAYED
        self.artifact_state = ArtifactState.ACTIVE
        return {
            'card_played': self.name,
            'mana_used':   self.cost,
            'effect':      f'Permanent: {self.effect.value}',
        }

    def activate_ability(self) -> dict[str, Any]:
        if self.age_effect == 0:
            self.artifact_state = ArtifactState.DESTROYED
            return {
                'artifact':  self.name,
                'activated': False,
                'reason':    'Artifact destroyed',
                'state':     self.artifact_state.value,
            }
        else:
            self.age_effect -= 1
            return {
                'artifact':            self.name,
                'ability_triggered':   self.effect.value,
                'durability_remaining': self.age_effect,
                'activated':           True,
                'state':               self.artifact_state.value,
            }
