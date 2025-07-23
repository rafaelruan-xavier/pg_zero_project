from pgzero import keyboard
from core.entities.Hero import Hero
from core.repository.ICharacterMovement import ICharacterMovement

class MoveCharacterUseCase:
    def __init__(self, icharacter_movement: ICharacterMovement): # type: ignore
        self.__movement_service = icharacter_movement

    def execute(self, keyboard: keyboard):
        self.__movement_service.input_character_movement(keyboard)
        