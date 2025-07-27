#---------- IMPORTS OF CORE PACKAGE ----------
from core.enums import WindowGameEnum
from core.enums import HeroEnum
from core.enums import CharacterEnum
from core.enums import MusicEnum
from core.entities.Alien import Alien
from core.entities.CharacterPosition import CharacterPosition
from core.entities.Hero import Hero
from core.enums import ImagesEnum
from core.enums import GameStateEnum

#---------- IMPORTS OF USE CASE PACKAGE ----------
from application.use_cases.MoveEnemyUseCase import MoveEnemyUseCase
from application.use_cases.MoveHeroUseCase import MoveHeroUseCase
from application.use_cases.MusicUseCase import MusicUseCase
from application.use_cases.MainMenuUseCase import MainMenuUseCase

#---------- IMPORTS OF SERVICES PACKAGE ----------
from infrastructure.services.MovementService import MovementService
from infrastructure.services.MovementHeroService import MovementHeroService
from infrastructure.services.MovementEnemyService import MovementEnemyService
from infrastructure.services.MusicService import MusicService
from infrastructure.services.MainMenuService import MainMenuService
from infrastructure.services.ScreenService import ScreenService

#---------- IMPORTS OF PGZERO ----------
from pgzero.actor import Actor
from pgzero import clock


#----------- CONFIG ----------
WIDTH = WindowGameEnum.WIDTH
HEIGHT = WindowGameEnum.HEIGHT
FRAME_ENEMY_NAMES = [
    ImagesEnum.MAGE_IDLE_FRAME1,
    ImagesEnum.MAGE_IDLE_FRAME2,
    ImagesEnum.MAGE_IDLE_FRAME3,
    ImagesEnum.MAGE_IDLE_FRAME4,
    ImagesEnum.MAGE_IDLE_FRAME5,
    ImagesEnum.MAGE_IDLE_FRAME6,
    ImagesEnum.MAGE_IDLE_FRAME7,
    ImagesEnum.MAGE_IDLE_FRAME8
]

DICT_HERO_FRAME_NAMES_FOR_EACH_DIRECTION = {
    "right": [ImagesEnum.HERO_RIGHT1_ANIMATION, ImagesEnum.HERO_RIGHT2_ANIMATION],
    "left": [ImagesEnum.HERO_LEFT1_ANIMATION, ImagesEnum.HERO_LEFT2_ANIMATION],
    "up": [ImagesEnum.HERO_UP1_ANIMATION],
    "down": [ImagesEnum.HERO_DOWN1_ANIMATION, ImagesEnum.HERO_DOWN2_ANIMATION],
    "idle": [ImagesEnum.HERO_IDLE_ANIMATION]
}

current_game_state = GameStateEnum.MENU
menu_music_started = False
music_game_started = False
#----------- INSTANCES -----------
hero_instance = None
hero_movement_instance = None
hero_position_instance = CharacterPosition()
hero_actor_pgzero_instance = Actor(ImagesEnum.HERO_IDLE_ANIMATION) 

alien1_instance = None
alien1_movement_instance = None
alien1_position_instance = CharacterPosition(WindowGameEnum.TOP_MIDLE_POSITION)
alien1_actor_pgzero_instance = Actor(ImagesEnum.MAGE_IDLE_FRAME1)

music_service = None
music_use_case = None

main_menu_service = None
main_menu_use_case = None

#----------- IMPLEMENTATIONS -----------
hero_instance = Hero(
    hero_actor_pgzero_instance, 
    HeroEnum.NAME, # Zeca
    CharacterEnum.DEFAULT_LIFE_START_GAME, # 100
    hero_position_instance, 
    HeroEnum.SPEED) # 10
hero_movement_instance = MoveHeroUseCase(MovementHeroService(hero_instance, DICT_HERO_FRAME_NAMES_FOR_EACH_DIRECTION))

alien1_instance = Alien(
    alien1_actor_pgzero_instance,
    HeroEnum.NAME,
    CharacterEnum.DEFAULT_LIFE_START_GAME,
    alien1_position_instance,
    6
)
alien1_movement_instance = MoveEnemyUseCase(MovementEnemyService(alien1_instance))

music_service = MusicService()
music_use_case = MusicUseCase(music_service)

main_menu_service = MainMenuService()
main_menu_use_case = MainMenuUseCase(main_menu_service)
#---------- RUN -----------

def draw():
    global current_game_state
    
    if current_game_state == GameStateEnum.MENU:
        screen.clear()
        main_menu_use_case.execute_draw(screen, music_use_case)
        
    elif current_game_state == GameStateEnum.RUNNING:
        screen.clear()
        screen.fill(WindowGameEnum.BACKGROUND_COLOR_GRAY) 
        hero_instance.get_actor().draw()
        alien1_instance.get_actor().draw()
        screen.draw.text(f"Hero Life: {hero_instance.get_life()}", (10, 10), fontsize=30, color="white")

def update():
    global current_game_state
    global menu_music_started
    
    if current_game_state == GameStateEnum.MENU:
        result = main_menu_service.handle_input(keyboard, music_use_case)

        if result == "stop_music":
            music_use_case.execute_stop()
            menu_music_started = False
            current_game_state = GameStateEnum.MENU

        elif result == "play_music":
            music_use_case.execute_play(MusicEnum.INITIAL_MENU)
            menu_music_started = True
            current_game_state = GameStateEnum.MENU
        elif result == "running":
            current_game_state = GameStateEnum.RUNNING
    elif current_game_state == GameStateEnum.RUNNING:
        if menu_music_started:
            music_use_case.execute_stop()
            menu_music_started = False
            music_use_case.execute_play(MusicEnum.GAME_RUNNING)
       

        hero_movement_instance.execute(keyboard)
        alien1_movement_instance.execute_movement_towards_hero(hero_position_instance, hero_instance)
        alien1_movement_instance.execute_update_enemy_idle_animation(FRAME_ENEMY_NAMES, alien1_actor_pgzero_instance)
