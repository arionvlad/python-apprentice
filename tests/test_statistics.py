from python_apprentice.statistics import mean, median


def test_mean() -> None:
    assert mean([1.0, 2.0, 3.0, 4.0]) == 2.5
    assert mean([5.5]) == 5.5


def test_mean_empty_list_raises() -> None:
    try:
        mean([])
    except ValueError as exc:
        assert str(exc) == "mean requires at least one number"
    else:
        raise AssertionError("Expected ValueError for empty input")


def test_median_odd_count() -> None:
    assert median([3.0, 1.0, 2.0]) == 2.0


def test_median_even_count() -> None:
    assert median([1.0, 4.0, 2.0, 3.0]) == 2.5


def test_median_empty_list_raises() -> None:
    try:
        median([])
    except ValueError as exc:
        assert str(exc) == "median requires at least one number"
    else:
        raise AssertionError("Expected ValueError for empty input")
