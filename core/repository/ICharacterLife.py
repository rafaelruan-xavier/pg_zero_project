#----------- IMPORTS OF ENTITIES PACKAGE ----------
from core.entities.Character import Character


class ICharacterLife:

    """Interface/contract that represents the actions for character life."""

    def increase_life(character: Character, life_increase_value: int):
        pass

    def decrease_life(character: Character, damage_value: int):
        pass