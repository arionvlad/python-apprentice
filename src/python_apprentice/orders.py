def calculate_subtotal(prices: list[float]) -> float:
    """Calculates the subtotal of a list of prices.
    Raises a ValueError if the list is empty or contains negative prices."""

    subtotal = 0.0
    if not prices:
        raise ValueError("Price list cannot be empty")
    for price in prices:
        if price < 0:
            raise ValueError("Price cannot be negative")
        else:
            subtotal += price
    return subtotal


def calculate_discount(subtotal: float, discount_percent: float) -> float:
    """Calculates the discount amount based on the subtotal and discount percentage.
    Raises a ValueError if the discount percentage is not between 0 and 100."""

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return subtotal * discount_percent / 100


def calculate_tax(amount: float, tax_percent: float) -> float:
    """Calculates the tax amount based on the amount and tax percentage.
    Raises a ValueError if the tax percentage is not between 0 and 100."""

    if tax_percent < 0 or tax_percent > 100:
        raise ValueError("Tax percent must be between 0 and 100")
    return amount * tax_percent / 100


def calculate_total(
    prices: list[float],
    discount_percent: float,
    tax_percent: float,
) -> float:
    """Calculates the total amount after applying discount and tax to the subtotal.
    Raises a ValueError if the price list is empty, contains negative prices,
    or if the discount or tax percentages are invalid."""

    subtotal = calculate_subtotal(prices)
    discount = calculate_discount(subtotal, discount_percent)
    tax = calculate_tax(subtotal - discount, tax_percent)
    return subtotal - discount + tax
