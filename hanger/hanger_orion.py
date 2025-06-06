from abc import abstractmethod


class HangarSystem:
    @abstractmethod
    def dock_ship(self, ship_id: str, ship_type: str) -> bool:
        """Dock a ship. Returns True if successful."""
        pass

    @abstractmethod
    def undock_ship(self, ship_id: str) -> bool:
        """Undock a ship. Returns True if successful."""
        pass

    @abstractmethod
    def perform_maintenance(self, ship_id: str) -> dict:
        """Run maintenance routines on a docked ship."""
        pass

    @abstractmethod
    def list_docked_ships(self) -> list:
        """Return a list of currently docked ships."""
        pass

    @abstractmethod
    def supported_ship_types(self) -> list:
        """Return a list of supported ship types for this hangar."""
        pass