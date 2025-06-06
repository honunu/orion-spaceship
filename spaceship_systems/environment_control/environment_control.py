from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class EnvironmentalControl(SystemModule):
    @abstractmethod
    def set_temperature(self, celsius: float) -> None:
        pass

    @abstractmethod
    def control_lighting(self, location: str, mode: str) -> None:
        pass
