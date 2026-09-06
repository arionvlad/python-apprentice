import math

"""
This module provides functions for temperature conversions and area calculations.
Functions:
- celsius_to_fahrenheit(celsius: float) -> float: Converts Celsius to Fahrenheit.
- fahrenheit_to_celsius(fahrenheit: float) -> float: Converts Fahrenheit to Celsius.
- circle_area(radius: float) -> float: Calculates the area of a circle given its radius.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Temperature below -273.15°C is not physically possible.")
    if celsius > 1.42e32:
        raise ValueError(
            "Temperature above Planck Temperature is not physically reasonable"
        )
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if fahrenheit < -459.67:
        raise ValueError("Temperature below -459.67°F is not physically possible.")
    if fahrenheit > 2e32:
        raise ValueError(
            "Temperature above Planck Temperature is not physically reasonable"
        )
    return (fahrenheit - 32) * 5 / 9


def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2
