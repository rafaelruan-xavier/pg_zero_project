from abc import ABC
from pgzero.actor import Actor
from core.entities.CharacterPosition import CharacterPosition

class Character(ABC):
    def __init__(self, character_actor_object: Actor, name: str, life: float, character_position: CharacterPosition, speed: float):
        self.__name = name
        self.__life = life
        self.__character_actor_object = character_actor_object
        self.__character_position = character_position
        self.__character_actor_object.pos = self.__character_position.get_character_position("x"), self.__character_position.get_character_position("y")
        self.__speed = speed
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value: str):
        self.__name = value
        return None
    
    def get_life(self):
        return self.__life
    
    def set_life(self, value: float):
        self.__life = value
        return None
    
    def get_actor(self):
        return self.__character_actor_object
    
    def get_position(self):
        return [self.__character_position.get_character_position("x"), self.__character_position.get_character_position("y")]
    
    def set_position(self, field: str, value: float):
        self.__character_position.set_character_position(field, value)
        self.__character_actor_object.pos = (
            self.__character_position.get_character_position("x"),
            self.__character_position.get_character_position("y")
    )
        return None
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, value: float):
        self.__speed = value