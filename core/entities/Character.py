#------------ IMPORTS OF ENTITIES ------------
from core.entities.CharacterPosition import CharacterPosition

#------------ IMPORTS OF PGZERO ------------
from pgzero.actor import Actor


class Character:
    """Abstract class that represent a entity of character."""

    def __init__(self, character_actor_object: Actor, name: str, life: float, character_position: CharacterPosition, speed: float):

        """
        Initialize a new character.

        Args:
            character_actor_object (Actor): Receive a actor object of pgzero.
            name (str): Receive a character name.
            life (float): Receive a character life.
            character_position (CharacterPosition): Receive a character position object.
            speed (float): Receive a character speed.
        """

        self.__name = name
        self.__life = life
        self.__character_actor_object = character_actor_object
        self.__character_position = character_position
        self.__character_actor_object.pos = self.__character_position.get_character_position("x"), self.__character_position.get_character_position("y")
        self.__speed = speed
    
    def get_name(self):

        """Return name (str)."""

        return self.__name
    
    def set_name(self, value: str):

        """
        Apply a new name for this character.

        Args:
            value (str): New name for this character.
        """

        self.__name = value
        return None
    
    def get_life(self):

        """Return life (float)."""

        return self.__life
    
    def set_life(self, value: float):

        """
        Apply a new life for this character.

        Args:
            value (float): New value for the life.
        """

        self.__life = value
        return None
    
    def get_actor(self):

        """Return the actor (Actor) object of pgzero implemented in this character."""

        return self.__character_actor_object
    
    def get_position(self):

        """Return the character position object (CharacterPosition)"""

        return [self.__character_position.get_character_position("x"), self.__character_position.get_character_position("y")]
    
    def set_position(self, axle: str, value: float):

        """
        Apply a new position for this character.

        Args:
            axle (str): Is that about the X axle or Y axle.
            value (float): Value for the axle chosen.
        """

        self.__character_position.set_character_position(axle, value)
        self.__character_actor_object.pos = (
            self.__character_position.get_character_position("x"),
            self.__character_position.get_character_position("y")
    )
        return None
    
    def get_speed(self):

        """Return speed (str)."""

        return self.__speed
    
    def set_speed(self, value: float):
        """
        Apply a new speed for this character.

        Args:
            value (float): New value for speed.
        """
        self.__speed = value