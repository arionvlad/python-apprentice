from python_apprentice import greet


def test_greet_returns_personalized_message() -> None:
    assert greet("Vlad") == "Hello, Vlad!"
