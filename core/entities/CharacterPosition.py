#---------- IMPORTS OF ENUMS ----------
from core.enums import WindowGameEnum


class CharacterPosition:

    """Class that represent a entity of character position."""

    def __init__(self, tuple_x_y: tuple = (WindowGameEnum.WIDTH /2, WindowGameEnum.HEIGHT /2)):

        """Initialize a new object character position in the center of window game for default."""

        self._x = tuple_x_y[0]
        self._y = tuple_x_y[1]

    def get_character_position(self, axle: str):

        """
        Return the character position in the axle chosen.

        Args:
            axle (str): It's that about X axle or Y axle.
        """

        if (axle.lower() == WindowGameEnum.AXLE_X):
            return self._x
        elif (axle.lower() == WindowGameEnum.AXLE_Y):
            return self._y
        else:
            raise ValueError("Invalid value for axle in enemy_position.")
    
    def set_character_position(self, axle: str, value: float):

        """
        Redefine the character position in the axle chosen.

        Args:
            axle (str) = Receives the axle chosen -> x or y
            value (float) = New value for a position.
        """
        if (axle.lower() == WindowGameEnum.AXLE_X):
            self._x = value
        elif (axle.lower() == WindowGameEnum.AXLE_Y):
            self._y = value
        else:
            raise ValueError("Invalid value for axle in enemy_position.")
