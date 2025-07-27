#---------- IMPORTS OF CORE PACKAGE ----------
from core.enums.WindowGameEnum import WIDTH, HEIGHT

class ScreenService:

    """"""

    def __init__(self, pgzero_screen_object):
        self._pgzero_screen_object = pgzero_screen_object

    def draw_death_screen(self):
        self._pgzero_screen_object.clear()
        self._pgzero_screen_object.fill((10, 10, 10))


        self._pgzero_screen_object.draw.text("💀 GAME OVER 💀", center=(WIDTH // 2 + 2, HEIGHT // 3 + 2), fontsize=80, color="black")
        self._pgzero_screen_object.draw.text("💀 GAME OVER 💀", center=(WIDTH // 2, HEIGHT // 3), fontsize=80, color="red")
        self._pgzero_screen_object.draw.text("Press R to Restart", center=(WIDTH // 2 + 1, HEIGHT // 2 + 1), fontsize=40, color="black")
        self._pgzero_screen_object.draw.text("Press R to Restart", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="white")
