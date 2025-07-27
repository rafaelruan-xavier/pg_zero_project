#---------- IMPORTS OF CORE PACKAGE ----------
from core.repository.IMusicService import IMusicService

#---------- IMPORTS OF PGZERO ----------
from pgzero import music

class MusicService(IMusicService):

    """"""

    def __init__(self):
        pass

    def play(self, music_name: str):
        """
        """

        music.play(music_name)
        return None
    
    def stop(self):
        """
        """
        music.stop()
        return None
    
    def music_is_playing(self, music_name):
        return music.is_playing(music_name)
    
