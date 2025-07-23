
class CharacterPosition:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_character_position(self, field: str):
        if (field.lower() == "x"):
            return self._x
        elif (field.lower() == "y"):
            return self._y
        else:
            raise ValueError("Invalid value for field in enemy_position.")
    
    def set_character_position(self, field: str, value: float):
        if (field.lower() == "x"):
            self._x = value
        elif (field.lower() == "y"):
            self._y = value
        else:
            raise ValueError("Invalid value for field in enemy_position.")
