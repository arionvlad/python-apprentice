from python_apprentice.greetings import greet


def test_greet_returns_personalized_message() -> None:
    assert greet("Vlad") == "Hello, Vlad!"
