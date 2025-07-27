#------------ IMPORTS OF CORE PACKAGE ------------
from core.repository.ICharacterLife import ICharacterLife
from core.entities.Character import Character



class CharacterLifeService(ICharacterLife):

    

    def increase_life(character: Character, life_increase_value: int):

        """
        Method to increase character life

        Args:
            character (Character): Receive the any object of type Character.
            life_increase_value (float): Receive a value for increment in character life.
        """
        character.set_life(life_increase_value)

    
    def decrease_life(character: Character, life_decrease_value: int):

        """
        Method to decrease character life

        Args:
            character (Character): Receive the any object of type Character.
            life_decrease_value (float): Receive a value for decrease in character life.
        """
        character.set_life((-1) * (life_decrease_value))
    
