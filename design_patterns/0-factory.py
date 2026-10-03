#!/usr/bin/env python3
"""Factory pattern: a registry-based vehicle factory."""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Common interface for every vehicle."""

    @abstractmethod
    def mode(self) -> str:
        """Return the kind of lane or road the vehicle uses."""


class Bus(Vehicle):
    """A bus."""

    def mode(self) -> str:
        """Return the bus mode."""
        return "road"


class Train(Vehicle):
    """A train."""

    def mode(self) -> str:
        """Return the train mode."""
        return "rails"


class Bike(Vehicle):
    """A bike."""

    def mode(self) -> str:
        """Return the bike mode."""
        return "lane"


class Scooter(Vehicle):
    """A scooter."""

    def mode(self) -> str:
        """Return the scooter mode."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles by name using a registry of classes."""

    def __init__(self) -> None:
        """Start with the built-in vehicle kinds registered."""
        self._registry = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name: str, cls: type) -> None:
        """Map a name to a vehicle class."""
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        """Create a vehicle of the given kind."""
        try:
            cls = self._registry[kind]
        except KeyError:
            raise ValueError("Unknown vehicle kind: {}".format(kind))
        return cls()


def main() -> None:
    """Show the factory creating every registered vehicle."""
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
