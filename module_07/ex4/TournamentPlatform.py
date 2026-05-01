from enum import Enum
from ex4.TournamentCard import TournamentCard


class PlatformStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class TournamentPlatform:

    def __init__(self) -> None:
        self.cards: dict = {}
        self.matches: list = []
        self.match_count: int = 0
        self.status: PlatformStatus = PlatformStatus.ACTIVE

    def register_card(self, card: TournamentCard) -> str:
        id = f"{card.name.lower().replace(' ', '_')}_{len(self.cards) + 1:03}"
        self.cards[id] = card
        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winer, loser = card1, card2
            winer_id, loser_id = card1_id, card2_id
        else:
            winer, loser = card2, card1
            winer_id, loser_id = card2_id, card1_id
        winer.update_wins(1)
        loser.update_losses(1)
        self.matches.append({'winner': winer_id, 'loser': loser_id})
        return {
            'winner': winer_id,
            'loser': loser_id,
            'winner_rating': winer.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        rs: list = []
        for card_id, card in self.cards.items():
            rs.append({
                'id': card_id,
                'name': card.name,
                'rating': card.rating,
                'record': f'{card.wins}-{card.losses}'
            })
        for i in range(len(rs)):
            for j in range(i + 1, len(rs)):
                if rs[i]['rating'] < rs[j]['rating']:
                    rs[i], rs[j] = rs[j], rs[i]
        return rs

    def generate_tournament_report(self) -> dict:
        total: int = len(self.cards)
        avg: float = sum(c.rating for c in self.cards.values()) / total
        return {
            'total_cards': total,
            'matches_played': len(self.matches),
            'avg_rating': int(avg),
            'platform_status': self.status.value
        }
