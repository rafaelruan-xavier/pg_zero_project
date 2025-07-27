#---------- IMPORTS OF CORE -----------
from core.entities.Enemy import Enemy


class Alien(Enemy):

    """Class of type Character that represents the Alien."""
    
    def __init__(self, actor_object, name, life, character_position, speed): # type: ignore
        super().__init__(actor_object, name, life, character_position, speed)

