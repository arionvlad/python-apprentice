from python_apprentice.math_utils import (
    celsius_to_fahrenheit,
    circle_area,
    fahrenheit_to_celsius,
)


def test_celsius_to_fahrenheit() -> None:
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40


def test_celsius_to_fahrenheit_positive_fraction() -> None:
    assert celsius_to_fahrenheit(25.5) == 77.9


def test_fahrenheit_to_celsius() -> None:
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40


def test_fahrenheit_to_celsius_positive_fraction() -> None:
    assert fahrenheit_to_celsius(77.9) == 25.5


def test_circle_area() -> None:
    assert circle_area(1) == 3.141592653589793
    assert circle_area(0) == 0
    assert circle_area(2) == 12.566370614359172


def test_circle_area_fractional_radius() -> None:
    assert circle_area(0.5) == 0.7853981633974483


def test_circle_area_negative_radius() -> None:
    assert circle_area(-2) == 12.566370614359172


def test_temperature_conversion_round_trip() -> None:
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == 37
