#---------- IMPORTS OF ENUMS ----------
from core.enums.WindowGameEnum import HEIGHT as window_game_height
from core.enums.WindowGameEnum import WIDTH as window_game_width


class CharacterPosition:

    """Class that represent a entity of character position."""

    def __init__(self, 
                 x: float = window_game_width /2, 
                 y: float =  window_game_height /2):

        """Initialize a new object character position in the center of window game for default."""

        self._x = x
        self._y = y

    def get_character_position(self, axle: str):

        """
        Return the character position in the axle chosen.

        Args:
            axle (str): It's that about X axle or Y axle.
        """

        if (axle.lower() == "x"):
            return self._x
        elif (axle.lower() == "y"):
            return self._y
        else:
            raise ValueError("Invalid value for axle in enemy_position.")
    
    def set_character_position(self, axle: str, value: float):
        if (axle.lower() == "x"):
            self._x = value
        elif (axle.lower() == "y"):
            self._y = value
        else:
            raise ValueError("Invalid value for axle in enemy_position.")
