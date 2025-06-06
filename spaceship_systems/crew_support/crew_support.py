from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class CrewSupport(SystemModule):
    @abstractmethod
    def serve_meal(self, crew_id: str, meal_type: str) -> None:
        pass

    @abstractmethod
    def schedule_shower(self, crew_id: str) -> None:
        pass
