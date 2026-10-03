#!/usr/bin/env python3
"""Decorator pattern: beverages extended by wrapping toppings."""
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Common interface for beverages and their decorators."""

    @abstractmethod
    def cost(self) -> int:
        """Return the cost in cents."""

    @abstractmethod
    def description(self) -> str:
        """Return the description."""


class Coffee(Beverage):
    """A plain coffee."""

    def cost(self) -> int:
        """Return the cost of a plain coffee."""
        return 50

    def description(self) -> str:
        """Return the description of a plain coffee."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Wrap another beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus the milk."""
        return self._inner.cost() + 10

    def description(self) -> str:
        """Return the wrapped description plus milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Wrap another beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus the sugar."""
        return self._inner.cost() + 5

    def description(self) -> str:
        """Return the wrapped description plus sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Wrap another beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return the wrapped cost plus the caramel."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Return the wrapped description plus caramel."""
        return self._inner.description() + " + caramel"


def main() -> None:
    """Build three beverages and print their description and cost."""
    drinks = [
        MilkDecorator(Coffee()),
        MilkDecorator(SugarDecorator(Coffee())),
        CaramelDecorator(MilkDecorator(SugarDecorator(Coffee()))),
    ]
    for drink in drinks:
        print(drink.description(), drink.cost())


if __name__ == "__main__":
    main()
