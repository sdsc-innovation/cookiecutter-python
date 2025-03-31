import keyword
import re
import sys


SLUG_REGEX = r"[a-z]([a-z0-9\-]*[a-z0-9])?"


def is_slug(name: str) -> bool:
    return re.fullmatch(SLUG_REGEX, name) is not None


def is_identifier(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def is_module_name(name: str) -> bool:
    return is_identifier(name) and name.islower()


PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"


if not is_slug(PROJECT_SLUG):
    print(
        "ERROR: invalid project slug, must be kebab-case (lowercase alphanumeric and "
        "dashes)"
    )
    sys.exit(1)

if not is_module_name(MODULE_NAME):
    print(
        "ERROR: invalid module name, must be a valid Python identifier in snake_case "
        "(lowercase alphanumeric and underscores)"
    )
    sys.exit(2)
