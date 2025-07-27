#---------- IMPORTS OF CORE PACKAGE ----------
from core.repository.IMenu import IMenu
from core.enums import MusicEnum

#---------- IMPORTS OF CORE PACKAGE ----------
from core.enums import WindowGameEnum
from core.enums import GameStateEnum

#----------- IMPORTS OF APPLICATION PACKAGE -----------
from application.use_cases.MusicUseCase import MusicUseCase



class MainMenuService(IMenu):

    """"""
    def __init__(self):
        pass

    def draw(self, screen, music_use_case: MusicUseCase):
        #music_use_case.execute_play(MusicEnum.INITIAL_MENU)
        screen.fill(WindowGameEnum.BACKGROUND_COLOR_GRAY)
        screen.draw.text("🚨 ESCAPE THE MONSTER 🚨", center=(WindowGameEnum.WIDTH // 2, WindowGameEnum.HEIGHT // 4), fontsize=60, color="red")
        screen.draw.text("Press Enter to Start", center=(WindowGameEnum.WIDTH // 2, WindowGameEnum.HEIGHT // 2), fontsize=40, color="white")
        screen.draw.text("Press Esc to Exit", center=(WindowGameEnum.WIDTH // 2, WindowGameEnum.HEIGHT // 2 + 60), fontsize=40, color="white")
        screen.draw.text("Press C to START/STOP the music.", center=(WindowGameEnum.WIDTH // 2, WindowGameEnum.HEIGHT // 2 + 90), fontsize=30, color="white")
    
    def handle_input(self, keyboard, music_use_case: MusicUseCase):
        if keyboard.RETURN:
            return GameStateEnum.RUNNING
        elif keyboard.escape:
            exit()
        elif keyboard.c:
            if music_use_case.execute_music_is_playing(MusicEnum.INITIAL_MENU):
                print("chamou!")
                return "stop_music"
            else:
                return "play_music"
        else:
            return GameStateEnum.MENU

    