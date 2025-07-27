#------------ IMPORTS OF USE CASE ------------
from application.use_cases.MoveCharacterUseCase import MoveCharacterUseCase

#------------ IMPORTS OF PGZERO ------------
from pgzero import keyboard

class MoveHeroUseCase(MoveCharacterUseCase):

    """Class that represents the use case of hero movement."""

    def __init__(self, icharacter_movement):

        """
        Initialize a new object of use case hero movement.

        Args:
            icharacter_movement (ICharacterMovement): Receive any object that implements the interface ICharacterMovement.
        """

        super().__init__(icharacter_movement)
    
    def execute(self, keyboard: keyboard):

        """
        Calls a implementation/service that can read the keyboard input and execute the moviment.

        Args:
            keyboard (keyboard): Receive the keyboard object of pgzero.   
        """

        super().get_movement_service().identify_input_keyboard_and_decide(keyboard)
        return None
