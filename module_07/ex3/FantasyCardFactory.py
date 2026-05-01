from typing import Any
from ex3.CardFactory import CardFactory, CreatureType, SpellType, ArtifactType
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card, Rarity
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard, ArtifactEffect


class FantasyCardFactory(CardFactory):

    def get_supported_types(self) -> dict[str, Any]:
        return {
            'creatures': [t.value for t in CreatureType],
            'spells':    [t.value for t in SpellType],
            'artifacts': [t.value for t in ArtifactType],
        }

    def create_creature(
            self,
            name_or_power: CreatureType | None = None
    ) -> Card:
        if name_or_power == CreatureType.GOBLIN:
            return CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 3, 2)
        else:
            return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    def create_spell(self, name_or_power: SpellType | None = None) -> Card:
        if name_or_power == SpellType.FIREBALL:
            return SpellCard(
                "Lightning Bolt", 3, Rarity.RARE, EffectType.DAMAGE
            )
        else:
            return SpellCard(
                "Fireball", 4, Rarity.RARE, EffectType.DAMAGE
            )

    def create_artifact(
            self,
            name_or_power: ArtifactType | None = None
    ) -> Card:
        if name_or_power == ArtifactType.MANA_RING:
            return ArtifactCard(
                "Mana Ring", 2, Rarity.RARE, 3, ArtifactEffect.BOOST
            )
        else:
            return ArtifactCard(
                "Mana Crystal", 2, Rarity.COMMON, 3, ArtifactEffect.BOOST
            )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature())
            elif i % 3 == 1:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {'cards': deck, 'size': len(deck)}
