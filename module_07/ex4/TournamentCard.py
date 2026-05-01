from ex4.Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable
from typing import Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200

    def play(self, game_state: dict[str, Any]) -> dict:
        game_state['card_played'] = self.name
        game_state['mana_used'] = self.cost
        game_state['effect'] = 'Tournament card enters battlefield'
        return game_state

    def attack(self, target: list) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_power,
            'combat_type': 'tournament'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_block = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - damage_block

        return {
            'defender': self.name,
            'damage_blocked': damage_block,
            'damage_taken': damage_taken,
            'still_alive': damage_taken < incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack_power': self.attack_power,
            'defense': self.defense,
            'combat_type': 'tournament'
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses,
            'record': f'{self.wins}-{self.losses}'
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'record': f'{self.wins}-{self.losses}',
            'interfaces': ['Card', 'Combatable', 'Rankable']
        }
