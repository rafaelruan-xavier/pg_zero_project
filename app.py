from pgzero.actor import Actor
from core.enums import WindowGame
from core.entities.Alien import Alien
from core.entities.CharacterPosition import CharacterPosition
from application.use_cases.MoveCharacterUseCase import MoveCharacterUseCase
from infrastructure.services.MovementService import MovementService


WIDTH = WindowGame.WIDTH
HEIGHT = WindowGame.HEIGHT

character_position = CharacterPosition(200, 300)
alien = Alien(Actor("shipbeige_manned.png"), "ship", 100, character_position, 10)
alien_movement_use_case = MoveCharacterUseCase(MovementService(alien))

def draw():
    screen.fill(WindowGame.BACKGROUND_COLOR_GRAY) # type: ignore
    alien.get_actor().draw()

def update():
    alien_movement_use_case.execute(keyboard)