#------------ IMPORTS OF CORE PACKAGE -------------
from core.entities.Character import Character
from core.enums import WindowGameEnum


#------------ IMPORTS OF REPOSITORY PACKAGE --------------
from core.repository.ICharacterMovement import ICharacterMovement



class MovementService(ICharacterMovement):

    """Class of type ICharacterMovement that represents the execution of movement."""

    def __init__(self, character: Character):

        """
        Initialize a new object of movement service.

        Args:
            character (Character): Receive any object of type Character.
        """

        self.__character = character

    def move_to_left(self):

        """Redefine the character position to left based in it's speed."""

        self.__character.set_position(WindowGameEnum.AXLE_X, self.__character.get_position()[0] - self.__character.get_speed())
        return None
    
    def move_to_right(self):

        """Redefine the character position to right based in it's speed."""
        
        self.__character.set_position(WindowGameEnum.AXLE_X, self.__character.get_position()[0] + self.__character.get_speed())
        return None

    def move_to_down(self):

        """Redefine the character position to down based in it's speed."""

        self.__character.set_position(WindowGameEnum.AXLE_Y, self.__character.get_position()[1] + self.__character.get_speed())
        return None
    
    def move_to_up(self):

        """Redefine the character position to up based in it's speed."""

        self.__character.set_position(WindowGameEnum.AXLE_Y, self.__character.get_position()[1] - self.__character.get_speed())
        return None

    def identify_input_keyboard_and_decide(self, keyboard):

        """
        Identify the input of keyboard and decide the character direction.

        Args:
            keyboard (keyboard): Receive a keyboard object of pgzero.
        """

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

    def get_character(self):

        """Returns the character object."""

        return self.__character

    def get_list_movement_functions(self):

        """Returns a list of functions reference."""

        list_movement_functions = [self.move_to_down, self.move_to_up, self.move_to_left, self.move_to_right]
        return list_movement_functions
