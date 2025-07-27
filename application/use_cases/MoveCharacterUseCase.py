#----------- IMPORTS OF CORE ------------
from core.entities.Hero import Hero


class MoveCharacterUseCase:

    """Class that represents the use case of character movement."""

    def __init__(self, interface_movement: None):

        """
        Initialize a new object of use case character movement.

        Args:
            interface_movement (None): Receive any object that implements a interface of moviment.
        """

        self.__movement_service = interface_movement

    def get_movement_service(self):

        """Returns the movement service object."""
        return self.__movement_service
    
    def execute():
        pass