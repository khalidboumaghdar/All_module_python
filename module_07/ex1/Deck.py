from enum import Enum
from typing import Optional, Any
from ex0.Card import Card
import random


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Deck:

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        try:
            total_cost = 0
            counts = {card_type: 0 for card_type in CardType}

            for card in self.cards:
                type_card = card.get_card_info()['type']
                for card_type in CardType:
                    if type_card == card_type.value:
                        counts[card_type] += 1
                total_cost += card.cost

            total = len(self.cards)
            avg_cost = round(total_cost / total, 1) if total > 0 else 0

            return {
                'total_cards': total,
                'creatures':   counts[CardType.CREATURE],
                'spells':      counts[CardType.SPELL],
                'artifacts':   counts[CardType.ARTIFACT],
                'avg_cost':    avg_cost,
            }
        except Exception as e:
            print(e)
