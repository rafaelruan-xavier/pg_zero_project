from core.entities.Character import Character
from core.entities.CharacterPosition import CharacterPosition

class Alien(Character):
    def __init__(self, actor_object, name, life, character_position, speed): # type: ignore
        super().__init__(actor_object, name, life, character_position, speed)

