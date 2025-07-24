#------------ IMPORTS OF USE CASE PACKAGE ------------
from application.use_cases.MoveCharacterUseCase import MoveCharacterUseCase


class MoveEnemyUseCase(MoveCharacterUseCase):

    """Class that represents the use case of enemy movement."""

    def __init__(self, iEnemyMovement):

        """
        Initialize a new object of use case hero movement.

        Args:
            icharacter_movement (ICharacterMovement): Receive any object that implements the interface ICharacterMovement.
        """

        super().__init__(iEnemyMovement)
    
    def execute(self, hero_position):

        """Execute the method to move enemy towards hero in MovementEnemyService."""
        self.get_movement_service().move_towards_hero(hero_position)
