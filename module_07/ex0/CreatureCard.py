from enum import Enum
from typing import Any
from ex0.Card import Card, CardState, Rarity


class CombatResult(Enum):
    WIN = "Win"
    LOSE = "Lose"
    DRAW = "Draw"


class CreatureCard(Card):

    def __init__(
        self,
        name:   str,
        cost:   int,
        rarity: Rarity,
        attack: int,
        health: int,
    ) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def get_card_info(self) -> dict[str, Any]:
        info: dict = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        self.state = CardState.PLAYED
        return {
            'card_played': self.name,
            'mana_used':   self.cost,
            'effect':      'Creature summoned to battlefield',
        }

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        if self.attack > target.health:
            result = CombatResult.WIN
        elif self.attack < target.health:
            result = CombatResult.LOSE
        else:
            result = CombatResult.DRAW

        return {
            'attacker':        self.name,
            'target':          target.name,
            'damage_dealt':    self.attack,
            'combat_resolved': True,
            'result':          result.value,
        }
