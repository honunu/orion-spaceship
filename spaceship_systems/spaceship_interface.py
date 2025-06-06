from abc import ABC, abstractmethod


class SystemModule(ABC):
    @abstractmethod
    def status(self) -> dict:
        """Return the current status of the system."""
        pass

    @abstractmethod
    def perform_diagnostics(self) -> dict:
        """Run diagnostics and return results."""
        pass
