from typing import Any
from ex3.GameStrategy import GameStrategy, StrategyName


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> StrategyName:
        return StrategyName.AGGRESSIVE

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict[str, Any]:
        name_cards = []
        use_mana = 0
        damage = 0

        for card in hand:
            name_cards.append(card.name)
            use_mana += card.cost
            damage += card.cost

        return {
            'strategy': self.get_strategy_name().value,
            'actions': {
                'cards_played':     name_cards,
                'mana_used':        use_mana,
                'targets_attacked': ['Enemy Player'],
                'damage_dealt':     damage,
            }
        }
