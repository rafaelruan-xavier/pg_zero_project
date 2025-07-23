from core.entities.Character import Character

class Hero(Character):

    def __init__(self, character_actor_object, name, life, character_position, speed):
        super().__init__(character_actor_object, name, life, character_position, speed)
        