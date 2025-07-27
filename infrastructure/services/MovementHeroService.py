#------------ IMPORTS OF CORE PACKAGE -------------
from core.enums import ImagesEnum

#---------- IMPORTS OF SERVICES PACKAGE ----------
from infrastructure.services.MovementService import MovementService

#---------- IMPORTS OF PGZERO ----------
from pgzero import clock

class MovementHeroService(MovementService):

    """Class that represents the execution of hero movement."""

    def __init__(self, character, dict_frames_for_each_direction: dict):
        super().__init__(character)
        self.__dict_frames_for_each_direction = dict_frames_for_each_direction
        self.__frame_index = 0
        self.__current_direction = "idle"
        clock.schedule_interval(self.update_hero_animation_for_direction, 0.17)
        

    #Override
    def identify_input_keyboard_and_decide(self, keyboard):

        """
        Identify the input of keyboard and decide the character direction.

        Args:
            keyboard (keyboard): Receive a keyboard object of pgzero.
        """

        if keyboard.left:
            self.move_to_left()
            self.__current_direction = "left"
        elif keyboard.right:
            self.move_to_right()
            self.__current_direction = "right"
        elif keyboard.up:
            self.move_to_up()
            self.__current_direction = "up"
        elif keyboard.down:
            self.move_to_down()
            self.__current_direction = "down"
        else:
            self.__current_direction = "idle"
    
    def update_hero_animation_for_direction(self):
        
        """
        """

        list_hero_frame_names = self.__dict_frames_for_each_direction[self.__current_direction]
        self.__frame_index = (self.__frame_index + 1) % len(list_hero_frame_names)
        super().get_character().get_actor().image = list_hero_frame_names[self.__frame_index]
        return None