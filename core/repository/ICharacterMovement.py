from abc import ABC, abstractmethod
from core.entities.Hero import Hero

class ICharacterMovement(ABC):

    @abstractmethod
    def move_to_left():
        pass

    @abstractmethod
    def move_to_right():
        pass

    @abstractmethod
    def move_to_up():
        pass

    @abstractmethod
    def move_to_down():
        pass
