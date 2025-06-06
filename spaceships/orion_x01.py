from spaceship_systems.power.power import X01PowerSystem
from spaceship_systems.propulsion.propulsion import PropulsionDrive


class OrionX01:

    def __init__(self):
        self.power_system = X01PowerSystem(initial_power=100.0)
        self.propulsion = PropulsionDrive()

