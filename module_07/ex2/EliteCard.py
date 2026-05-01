from typing import Any
from ex0.Card import Card, Rarity, CardState
from ex2.Combatable import Combatable, CombatType
from ex2.Magical import Magical, MagicType


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self,
            name:         str,
            cost:         int,
            rarity:       Rarity,
            attack_power: int,
            defense:      int,
            mana:         int,
            combat_type:  CombatType = CombatType.MELEE,
            magic_type: MagicType = MagicType.ARCANE,
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.mana: int = mana
        self.combat_type:  CombatType = combat_type
        self.magic_type: MagicType = magic_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        self.state = CardState.PLAYED
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        game_state['effect'] = 'Elite card enters battlefield'
        return game_state

    def attack(self, target: list) -> dict[str, Any]:
        return {
            'attacker':    self.name,
            'target':      target.name,
            'damage':      self.attack_power,
            'combat_type': self.combat_type.value,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        return {
            'defender':      self.name,
            'damage_blocked': damage_blocked,
            'damage_taken':  damage_taken,
            'still_alive':   damage_taken < incoming_damage,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            'attack_power': self.attack_power,
            'defense':      self.defense,
            'combat_type':  self.combat_type.value,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict[str, Any]:
        return {
            'caster':     self.name,
            'spell':      spell_name,
            'targets':    [t.name for t in targets],
            'mana_used':  self.cost,
            'magic_type': self.magic_type.value,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana += amount
        return {
            'channeled':  amount,
            'total_mana': self.mana,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            'mana':        self.mana,
            'spell_power': self.attack_power,
            'magic_type':  self.magic_type.value,
        }
