from core.repository.ICharacterMovement import ICharacterMovement
from core.entities.Character import Character

class MovementService(ICharacterMovement):

    def __init__(self, character: Character):
        self.__character = character

    def move_to_left(self):
        self.__character.set_position("x", self.__character.get_position()[0] - self.__character.get_speed())
        return None
    
    def move_to_right(self):
        self.__character.set_position("x", self.__character.get_position()[0] + self.__character.get_speed())
        return None

    def move_to_down(self):
        self.__character.set_position("y", self.__character.get_position()[1] + self.__character.get_speed())
        return None
    
    def move_to_up(self):
        self.__character.set_position("y", self.__character.get_position()[1] - self.__character.get_speed())
        return None

    def input_character_movement(self, keyboard):
        if keyboard.left:
            self.move_to_left()
        elif keyboard.right:
            self.move_to_right()
        elif keyboard.up:
            self.move_to_up()
        elif keyboard.down:
            self.move_to_down()
        else:
            pass
