def mean(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("mean requires at least one number")

    return sum(numbers) / len(numbers)


"""Calculates the mean of a list of numbers. ValueError for empty input"""


def median(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("median requires at least one number")

    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    mid = count // 2

    if count % 2 == 1:
        return sorted_numbers[mid]

    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


"""Calculates the median of a list of numbers. ValueError for empty input"""
