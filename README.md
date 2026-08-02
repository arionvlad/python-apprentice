# Python Apprentice

## Questions

1. What is `pyproject.toml`?
2. Why does the `src` directory exist?
3. Why do we need `__init__.py`?
4. What belongs inside `.gitignore`?

## Answers

### `pyproject.toml`

pyproject.toml is a configuration file used by packaging tools, as well as other tools such as linters, type checkers, etc. There are three possible TOML tables in this file.

The [build-system] table is strongly recommended. It allows you to declare which build backend you use and which other dependencies are needed to build your project.
The [project] table is the format that most build backends use to specify your project’s basic metadata, such as the dependencies, your name, etc.
The [tool] table has tool-specific subtables, e.g., [tool.hatch], [tool.black], [tool.mypy]. We only touch upon this table here because its contents are defined by each tool. Consult the particular tool’s documentation to know what it can contain.


### `src`

The “src layout” deviates from the flat layout by moving the code that is intended to be importable (i.e. import awesome_package, also known as import packages) into a subdirectory. This subdirectory is typically named src/, hence “src layout”.

The src layout helps enforce that an editable installation is only able to import files that were meant to be importable.

The flat layout would add the other project files (eg: README.md, tox.ini) and packaging/tooling configuration files (eg: setup.py, noxfile.py) on the import path. This would make certain imports work in editable installations but not regular installations.

### `__init__.py`

Python’s special __init__.py file marks a directory as a regular Python package and allows you to import its modules. This file runs automatically the first time you import its containing package. You can use it to initialize package-level variables, define functions or classes, and structure the package’s namespace clearly for users.

### `.gitignore`

You can create a .gitignore file in your repository's root directory to tell Git which files and directories to ignore when you make a commit. To share the ignore rules with other users who clone the repository, commit the .gitignore file into your repository.