import pytest

from python_apprentice import orders


def test_calculate_total() -> None:
    items = [
        10.0,
        5.0,
    ]

    assert orders.calculate_total(
        items, discount_percent=0, tax_percent=0
    ) == pytest.approx(15.0)


def test_calculate_total_empty_list() -> None:
    with pytest.raises(ValueError, match="Price list cannot be empty"):
        prices: list[float] = []
        orders.calculate_total(prices, discount_percent=0, tax_percent=0)


def test_calculate_total_negative_price() -> None:
    items = [
        -10.0,
        5.0,
    ]

    with pytest.raises(ValueError, match="Price cannot be negative"):
        orders.calculate_total(items, discount_percent=0, tax_percent=0)


def test_calculate_total_invalid_discount() -> None:
    items = [
        10.0,
        5.0,
    ]

    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100"):
        orders.calculate_total(items, discount_percent=150, tax_percent=0)


def test_calculate_total_invalid_tax() -> None:
    items = [
        10.0,
        5.0,
    ]

    with pytest.raises(ValueError, match="Tax percent must be between 0 and 100"):
        orders.calculate_total(items, discount_percent=0, tax_percent=150)


def test_calculate_total_with_discount_and_tax() -> None:
    items = [
        10.0,
        5.0,
    ]
    assert orders.calculate_total(
        items, discount_percent=10, tax_percent=5
    ) == pytest.approx(14.175)
