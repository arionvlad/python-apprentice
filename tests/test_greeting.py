from python_apprentice import greet

"""Test the greet function."""


def test_greet_returns_personalized_message() -> None:
    assert greet("Vlad") == "Hello, Vlad!"
