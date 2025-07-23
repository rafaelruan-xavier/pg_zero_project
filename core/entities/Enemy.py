#---------- IMPORTS OF CORE ----------
from core.entities.Character import Character

class Enemy(Character):
    
    """Class of type Character that represents the Alien."""

    def __init__(self, character_actor_object, name, life, character_position, speed):
        super().__init__(character_actor_object, name, life, character_position, speed)