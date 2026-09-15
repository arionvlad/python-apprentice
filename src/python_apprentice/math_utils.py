import math


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.

    Raises:
        ValueError: for temperatures below absolute zero
    """

    if celsius < -273.15:
        raise ValueError("Temperature below -273.15°C is not physically possible.")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.

    Raises:
        ValueError: for temperatures below absolute zero

    """

    if fahrenheit < -459.67:
        raise ValueError("Temperature below -459.67°F is not physically possible.")
    return (fahrenheit - 32) * 5 / 9


def circle_area(radius: float) -> float:
    """Calculates the area of a circle given its radius.
    Raises:
        ValueError: for negative radius
    """

    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2
