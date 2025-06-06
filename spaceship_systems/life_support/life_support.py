from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class LifeSupport(SystemModule):
    @abstractmethod
    def adjust_oxygen_level(self, level: float) -> None:
        pass

    @abstractmethod
    def recycle_water(self) -> None:
        pass




