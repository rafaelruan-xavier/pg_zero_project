#------------ IMPORTS OF ENTITIES ------------
from core.entities.Character import Character

class Hero(Character):

    """Class of type Character that represents the Hero."""

    def __init__(self, character_actor_object, name, life, character_position, speed):
        super().__init__(character_actor_object, name, life, character_position, speed)
        