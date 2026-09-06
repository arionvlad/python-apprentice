import pytest

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
    assert celsius_to_fahrenheit(25.5) == pytest.approx(77.9)


def test_celsius_to_fahrenheit_rejects_below_absolute_zero() -> None:
    with pytest.raises(
        ValueError,
        match="Temperature below -273.15°C is not physically possible.",
    ):
        celsius_to_fahrenheit(-273.16)


def test_celsius_to_fahrenheit_rejects_unreasonable_temperature() -> None:
    with pytest.raises(
        ValueError,
        match="Temperature above 1,000,000°C is not physically reasonable.",
    ):
        celsius_to_fahrenheit(1_000_000.01)


def test_fahrenheit_to_celsius() -> None:
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40


def test_fahrenheit_to_celsius_positive_fraction() -> None:
    assert fahrenheit_to_celsius(77.9) == pytest.approx(25.5)


def test_fahrenheit_to_celsius_rejects_below_absolute_zero() -> None:
    with pytest.raises(
        ValueError,
        match="Temperature below -459.67°F is not physically possible.",
    ):
        fahrenheit_to_celsius(-459.68)


def test_fahrenheit_to_celsius_rejects_unreasonable_temperature() -> None:
    with pytest.raises(
        ValueError,
        match="Temperature above 1,000,000°F is not physically reasonable.",
    ):
        fahrenheit_to_celsius(1_000_000.01)


def test_circle_area() -> None:
    assert circle_area(1) == 3.141592653589793
    assert circle_area(0) == 0
    assert circle_area(2) == 12.566370614359172


def test_circle_area_fractional_radius() -> None:
    assert circle_area(0.5) == 0.7853981633974483


def test_circle_area_rejects_negative_radius() -> None:
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(-2)


def test_temperature_conversion_round_trip() -> None:
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == 37
