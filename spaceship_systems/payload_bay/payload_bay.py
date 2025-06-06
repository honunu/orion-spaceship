from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class PayloadBay(SystemModule):
    @abstractmethod
    def load_cargo(self, manifest: dict) -> None:
        pass

    @abstractmethod
    def activate_robotics(self, task: str) -> None:
        pass
