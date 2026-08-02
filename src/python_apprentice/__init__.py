"""app package."""

from __future__ import annotations


def greet(name: str) -> str:
    return f"Hello, {name}!"


from .main import main

__all__ = ["greet", "main"]
