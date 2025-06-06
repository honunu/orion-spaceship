from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class SecuritySafety(SystemModule):
    @abstractmethod
    def authorize_access(self, crew_id: str, area: str) -> bool:
        pass

    @abstractmethod
    def trigger_alarm(self, alarm_type: str) -> None:
        pass

