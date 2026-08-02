"""Application entrypoint."""

from __future__ import annotations

from . import greet


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()
