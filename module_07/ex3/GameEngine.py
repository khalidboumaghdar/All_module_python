from typing import Any
from ex3.CardFactory import CardFactory, CreatureType
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.hand: list = []

    def configure_engine(
        self,
        factory:  CardFactory,
        strategy: GameStrategy,
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            self.factory.create_creature(CreatureType.GOBLIN),
            self.factory.create_creature(),
            self.factory.create_spell(),
        ]

    def simulate_turn(self) -> dict[str, Any]:
        result = self.strategy.execute_turn(self.hand, [])
        self.turns_simulated += 1
        self.total_damage += result['actions']['damage_dealt']
        return result

    def get_engine_status(self) -> dict[str, Any]:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used':   self.strategy.get_strategy_name().value,
            'total_damage':    self.total_damage,
            'cards_created':   len(self.hand),
        }
