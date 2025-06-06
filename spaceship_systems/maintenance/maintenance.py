from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class MaintenanceDiagnostics(SystemModule):
    @abstractmethod
    def schedule_repair(self, system_name: str) -> None:
        pass

    @abstractmethod
    def get_maintenance_log(self) -> list:
        pass