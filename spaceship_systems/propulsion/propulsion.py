from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class PropulsionDrive(SystemModule):
    @abstractmethod
    def set_thrust(self, level: float) -> None:
        pass

    @abstractmethod
    def engage_warp(self, destination: str) -> None:
        pass

class X01PropulsionDrive(PropulsionDrive):
    def __init__(self):
        self.thrust_level = 0.0
        self.warp_engaged = False
        self.destination = None
        self.engine_health = "Nominal"

    def status(self):
        return {
            "thrust_level": self.thrust_level,
            "warp_engaged": self.warp_engaged,
            "destination": self.destination,
            "engine_health": self.engine_health
        }

    def perform_diagnostics(self):
        # Simulate diagnostics logic
        diagnostics = {
            "main_engine": "OK",
            "thrusters": "OK",
            "fuel_lines": "OK",
            "warp_core": "OK" if not self.warp_engaged else "ENGAGED"
        }
        return diagnostics

    def set_thrust(self, level: float):
        if 0.0 <= level <= 1.0:
            self.thrust_level = level
        else:
            raise ValueError("Thrust level must be between 0.0 and 1.0")

    def engage_warp(self, destination: str):
        if not self.warp_engaged:
            self.warp_engaged = True
            self.destination = destination
        else:
            raise RuntimeError("Warp drive is already engaged!")

    def disengage_warp(self):
        if self.warp_engaged:
            self.warp_engaged = False
            self.destination = None
        else:
            raise RuntimeError("Warp drive is not engaged.")

