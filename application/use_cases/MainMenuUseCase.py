#---------- IMPORTS OF CORE PACKAGE -----------
from core.repository.IMenu import IMenu

class MainMenuUseCase:

    """"""

    def __init__(self, main_menu_service: IMenu):
        self.__main_menu_service = main_menu_service

    def get_main_menu_service(self):
        return self.__main_menu_service

    def execute_draw(self, screen, music_use_case):
        self.get_main_menu_service().draw(screen, music_use_case)
        return None
    
    def execute_handle_input(self):
        return self.get_main_menu_service().handle_input(keyboard)