from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class CommandNavigation(SystemModule):
    @abstractmethod
    def set_course(self, destination: str) -> None:
        pass

    @abstractmethod
    def get_current_position(self) -> dict:
        pass