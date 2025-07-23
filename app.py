#---------- IMPORTS OF CORE PACKAGE ----------
from core.entities.CharacterPosition import CharacterPosition
from core.enums import WindowGameEnum
from core.entities.Hero import Hero
from core.enums import SpriteImageEnum
from core.enums import HeroEnum
from core.entities.Alien import Alien

#---------- IMPORTS OF USE CASE PACKAGE ----------
from application.use_cases.MoveCharacterUseCase import MoveCharacterUseCase

#---------- IMPORTS OF SERVICES PACKAGE ----------
from infrastructure.services.MovementService import MovementService

#---------- IMPORTS OF PGZERO ----------
from pgzero.actor import Actor


#----------- CONFIG ----------
WIDTH = WindowGameEnum.WIDTH
HEIGHT = WindowGameEnum.HEIGHT


#----------- INSTANCES -----------
hero_instance = None
hero_movement_instance = None
hero_position_instance = CharacterPosition()
hero_actor_pgzero_instance = Actor(SpriteImageEnum.HERO_DEFAULT) 

alien1_instance = None
alien1_movement_instance = None
alien1_position_instance = CharacterPosition(800, 650)
alien1_actor_pgzero_instance = Actor(SpriteImageEnum.HERO_DEFAULT)

#----------- IMPLEMENTATIONS -----------
hero_instance = Hero(
    hero_actor_pgzero_instance, 
    HeroEnum.NAME, # Zeca
    HeroEnum.DEFAULT_LIFE, # 100
    hero_position_instance, 
    HeroEnum.SPEED) # 10
hero_movement_instance = MoveCharacterUseCase(MovementService(hero_instance))

alien1_instance = Alien(
    alien1_actor_pgzero_instance,
    HeroEnum.NAME,
    HeroEnum.DEFAULT_LIFE,
    alien1_position_instance,
    5
)
alien1_movement_instance = MoveCharacterUseCase(MovementService(alien1_instance))

#---------- RUN -----------
def draw():
    screen.fill(WindowGameEnum.BACKGROUND_COLOR_GRAY) # type: ignore
    hero_instance.get_actor().draw()
    alien1_instance.get_actor().draw()

def update():
    hero_movement_instance.execute(keyboard)
    alien1_movement_instance.execute(keyboard)
