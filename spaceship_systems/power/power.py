from abc import abstractmethod

from spaceship_systems.spaceship_interface import SystemModule


class PowerSystem(SystemModule):
    @abstractmethod
    def distribute_power(self, allocations: dict) -> None:
        pass

    @abstractmethod
    def emergency_shutdown(self) -> None:
        pass


class X01PowerSystem(PowerSystem):
    def __init__(self, initial_power: float = 100.0):
        self.power = initial_power

    def get_available_power(self) -> float:
        return self.power

    def consume_power(self, amount: float):
        if amount > self.power:
            raise RuntimeError("Not enough power.")
        self.power -= amount

    def recharge(self, amount: float):
        self.power += amount

    def status(self):
        return {"power": self.power}

    def perform_diagnostics(self):
        return {"power": self.power}