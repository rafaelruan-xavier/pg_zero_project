#----------- IMPORTS OF CORE ------------
from core.entities.Hero import Hero
from core.repository.ICharacterMovement import ICharacterMovement

#------------ IMPORTS OF PGZERO ------------
from pgzero import keyboard


class MoveCharacterUseCase:

    """Class that represents the use case of character movement."""

    def __init__(self, icharacter_movement: ICharacterMovement):

        """
        Initialize a new object of use case character movement.

        Args:
            icharacter_movement (ICharacterMovement): Receive any object that implements the interface ICharacterMovement.
        """

        self.__movement_service = icharacter_movement

    def execute(self, keyboard: keyboard):

        """
        Calls a implementation/service that can read the keyboard input and execute the moviment.

        Args:
            keyboard (keyboard): Receive the keyboard object of pgzero.   
        """

        self.__movement_service.identify_input_keyboard_and_decide(keyboard)
        return None
        