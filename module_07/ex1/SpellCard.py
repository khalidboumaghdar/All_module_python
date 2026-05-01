from enum import Enum
from typing import Any
from ex0.Card import Card, Rarity, CardState


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):

    def __init__(
            self,
            name:        str,
            cost:        int,
            rarity:      Rarity,
            effect_type: EffectType,
    ) -> None:
        if not isinstance(effect_type, EffectType):
            raise ValueError("Effect type must be an EffectType enum member")
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_type: EffectType = effect_type
        self.consumed: bool = False

    def get_card_info(self) -> dict[str, Any]:
        effect_info = super().get_card_info()
        effect_info['type'] = 'Spell'
        effect_info['effect_type'] = self.effect_type.value
        effect_info['consumed'] = self.consumed
        return effect_info

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        self.consumed = True
        self.state = CardState.PLAYED

        if self.effect_type == EffectType.DAMAGE:
            effect = f'Deal {self.cost} damage to target'
        elif self.effect_type == EffectType.HEAL:
            effect = f'Heal target for {self.cost}'
        elif self.effect_type == EffectType.BUFF:
            effect = f'Buff target by {self.cost}'
        elif self.effect_type == EffectType.DEBUFF:
            effect = f'Debuff target by {self.cost}'
        else:
            effect = f'Spell effect: {self.effect_type.value}'

        return {
            'card_played': self.name,
            'mana_used':   self.cost,
            'effect':      effect,
        }

    def resolve_effect(self, targets: list) -> dict[str, Any]:
        effect_names = []
        for t in targets:
            try:
                effect_names.append(t.name)
            except Exception:
                effect_names.append(str(t))
        return {
            'spell':       self.name,
            'effect_type': self.effect_type.value,
            'targets':     effect_names,
            'resolved':    True,
        }
