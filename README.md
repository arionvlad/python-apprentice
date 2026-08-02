# Python Project Template


## Quenstions

What is pyproject.toml?
Why does src exist?
Why do we need __init__.py?
What belongs inside .gitignore?

## Answers

### pyproject.toml

pyproject.toml is a configuration file used by packaging tools, as well as other tools such as linters, type checkers, etc. There are three possible TOML tables in this file.

The [build-system] table is strongly recommended. It allows you to declare which build backend you use and which other dependencies are needed to build your project.
The [project] table is the format that most build backends use to specify your project’s basic metadata, such as the dependencies, your name, etc.
The [tool] table has tool-specific subtables, e.g., [tool.hatch], [tool.black], [tool.mypy]. We only touch upon this table here because its contents are defined by each tool. Consult the particular tool’s documentation to know what it can contain.


### src

The “src layout” deviates from the flat layout by moving the code that is intended to be importable (i.e. import awesome_package, also known as import packages) into a subdirectory. This subdirectory is typically named src/, hence “src layout”.

Here’s a breakdown of the important behaviour differences between the src layout and the flat layout:

The src layout requires installation of the project to be able to run its code, and the flat layout does not.
This means that the src layout involves an additional step in the development workflow of a project (typically, an editable installation is used for development and a regular installation is used for testing).

The src layout helps prevent accidental usage of the in-development copy of the code.
This is relevant since the Python interpreter includes the current working directory as the first item on the import path. This means that if an import package exists in the current working directory with the same name as an installed import package, the variant from the current working directory will be used. This can lead to subtle misconfiguration of the project’s packaging tooling, which could result in files not being included in a distribution.

The src layout helps avoid this by keeping import packages in a directory separate from the root directory of the project, ensuring that the installed copy is used.

The src layout helps enforce that an editable installation is only able to import files that were meant to be importable.
This is especially relevant when the editable installation is implemented using a path configuration file that adds the directory to the import path.

The flat layout would add the other project files (eg: README.md, tox.ini) and packaging/tooling configuration files (eg: setup.py, noxfile.py) on the import path. This would make certain imports work in editable installations but not regular installations.

### __init__.py

Python’s special __init__.py file marks a directory as a regular Python package and allows you to import its modules. This file runs automatically the first time you import its containing package. You can use it to initialize package-level variables, define functions or classes, and structure the package’s namespace clearly for users.

### .gitignore

You can create a .gitignore file in your repository's root directory to tell Git which files and directories to ignore when you make a commit. To share the ignore rules with other users who clone the repository, commit the .gitignore file into your repository.