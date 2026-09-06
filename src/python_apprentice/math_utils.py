import math


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Temperature below -273.15°C is not physically possible.")
    if celsius > 1e6:
        raise ValueError("Temperature above 1,000,000°C is not physically reasonable.")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if fahrenheit < -459.67:
        raise ValueError("Temperature below -459.67°F is not physically possible.")
    if fahrenheit > 1e6:
        raise ValueError("Temperature above 1,000,000°F is not physically reasonable.")
    return (fahrenheit - 32) * 5 / 9


def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2
