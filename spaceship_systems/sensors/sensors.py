from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class SensorSuite(SystemModule):
    @abstractmethod
    def read_internal_sensors(self) -> dict:
        pass

    @abstractmethod
    def read_external_sensors(self) -> dict:
        pass
