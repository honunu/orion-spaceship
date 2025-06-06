from hanger.hanger_orion import HangarSystem
from spaceships.orion_x01 import OrionX01


class HangerX1(HangarSystem):
    pass


hanger_x01 = HangerX1()
orion = OrionX01()

if hanger_x01.perform_maintenance(orion):

    hanger_x01.undock_ship(orion)
    print(f"All system checked, undock, to the galaxy~")

else:
    print(f"System check failure, run diagnose on all systems")


