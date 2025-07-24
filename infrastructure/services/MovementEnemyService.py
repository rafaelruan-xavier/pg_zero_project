#---------- IMPORTS OF CORE PACKAGE ----------
from core.entities.CharacterPosition import CharacterPosition
from core.enums import WindowGameEnum

#---------- IMPORTS OF SERVICES PACKAGE -----------
from infrastructure.services.MovementService import MovementService

#---------- IMPORTS OF REPOSITORY PACKAGE
from core.repository.IEnemyMovement import IEnemyMovement

#---------- UTILS IMPORTS -----------
from random import choice

#---------- IMPORTS OF PGZERO ----------
from pgzero import clock

class MovementEnemyService(MovementService, IEnemyMovement):

    """Class that represents the execution of enemy movement."""

    def __init__(self, character):

        """
        Initialize a new object of enemy movement service.

        Args:
            character (Character): Receive any object of type Character.
        """
        super().__init__(character)

    def move_towards_hero(self, hero_position: CharacterPosition):

        """
        Algorithm to move enemy towards hero.

        Args:
            hero_position (CharacterPosition): Receives the CharacterPosition object of the hero.
        """

        non_exact_proxemic_tolerance = 10 # Tolerance of the non exact proxemic with a hero.

        #------------ Getting the current position of the enemy and the hero -> To compare latter ------------
        x_enemy_now, y_enemy_now =  super().get_character().get_position()
        x_hero_now, y_hero_now = hero_position.get_character_position(WindowGameEnum.AXLE_X), hero_position.get_character_position(WindowGameEnum.AXLE_Y)

        #------------ Comparing the positions in axle x ------------
        if (abs(x_enemy_now - x_hero_now) > non_exact_proxemic_tolerance): 
            if (x_enemy_now < x_hero_now):
                self.move_to_right()
            elif (x_enemy_now > x_hero_now):
                self.move_to_left()
            elif (x_enemy_now == x_hero_now):
                pass
        
        #------------ Comparing the positions in axle y ------------
        if (abs(y_enemy_now - y_hero_now) > non_exact_proxemic_tolerance):
            if (y_enemy_now < y_hero_now):
                self.move_to_down()
            elif (y_enemy_now > y_hero_now):
                self.move_to_up()
            elif (y_enemy_now == y_hero_now):
                pass
