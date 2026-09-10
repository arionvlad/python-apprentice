import math


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Temperature below -273.15°C is not physically possible.")
    return (celsius * 9 / 5) + 32


"""Convert Celsius to Fahrenheit. ValueError for temperatures below absolute zero"""


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if fahrenheit < -459.67:
        raise ValueError("Temperature below -459.67°F is not physically possible.")
    return (fahrenheit - 32) * 5 / 9


"""Convert Fahrenheit to Celsius. ValueError for temperatures below absolute zero"""


def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2


"""Calculates the area of a circle given its radius. ValueError for negative radius"""
