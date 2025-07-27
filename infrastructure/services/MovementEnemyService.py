#---------- IMPORTS OF CORE PACKAGE ----------
from core.entities.CharacterPosition import CharacterPosition
from core.enums import WindowGameEnum
from core.enums import CharacterMovementToleranceEnum
from core.enums import MusicEnum

from core.entities.Hero import Hero

#---------- IMPORTS OF SERVICES PACKAGE -----------
from infrastructure.services.MovementService import MovementService
from infrastructure.services.CharacterLifeService import CharacterLifeService
from infrastructure.services.ScreenService import ScreenService

#---------- IMPORTS OF REPOSITORY PACKAGE
from core.repository.IEnemyMovement import IEnemyMovement

#---------- UTILS IMPORTS -----------
from random import choice

#---------- IMPORTS OF PGZERO ----------
from pgzero.actor import Actor


class MovementEnemyService(MovementService, IEnemyMovement):

    """Class that represents the execution of enemy movement."""

    def __init__(self, character):

        """
        Initialize a new object of enemy movement service.

        Args:
            character (Character): Receive any object of type Character.
        """
        super().__init__(character)
        self._frame_index_idle_animation = 0

    def move_towards_hero(self, hero_position: CharacterPosition, hero_instance: Hero):

        """
        Algorithm to move enemy towards hero.

        Args:
            hero_position (CharacterPosition): Receives the CharacterPosition object of the hero.
        """

        non_exact_proxemic_tolerance = CharacterMovementToleranceEnum.NON_EXACT_PROXEMIC # Tolerance of the non exact proxemic with a hero.
        damage_distance_threshold = CharacterMovementToleranceEnum.DAMAGE_RANGE_ENTRY_OBJECTS


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
        
        #---------- Checking if can apply damage ----------
        distance_x_between_enemy_hero = abs(x_enemy_now - x_hero_now)
        distance_y_between_enemy_hero = abs(y_enemy_now - y_hero_now)
        if (
            (distance_x_between_enemy_hero <= damage_distance_threshold) 
            and 
            (distance_y_between_enemy_hero <= damage_distance_threshold)):
            CharacterLifeService.decrease_life(hero_instance, 5)
        return None
    
    def update_enemy_idle_animation(self, enemy_frame_names: list, enemy_actor_pgzero_instance: Actor):

        """
        """

        self._frame_index_idle_animation = (self._frame_index_idle_animation + 1) % len(enemy_frame_names)
        enemy_actor_pgzero_instance.image = enemy_frame_names[self._frame_index_idle_animation]
