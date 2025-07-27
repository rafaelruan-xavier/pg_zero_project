#---------- IMPORTS OF CORE PACKAGE -----------
from core.repository.IMusicService import IMusicService


class MusicUseCase:

    """"""

    def __init__(self, music_service):
        """
        """

        self.music_service = music_service

    def execute_play(self, music_name: str):
        """
        """

        self.music_service.play(music_name)

    def execute_stop(self):
        """
        """

        self.music_service.stop()
    
    def execute_music_is_playing(self, music_name):
        return self.music_service.music_is_playing(music_name)
