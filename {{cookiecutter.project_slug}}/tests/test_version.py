import re

from {{ cookiecutter.module_name }} import __version__


SEMVER_REGEX = re.compile(
    r"""
    (0|[1-9]\d*) # Major
    \.
    (0|[1-9]\d*) # Minor
    \.
    (0|[1-9]\d*) # Revision
    """,
    re.VERBOSE,
)


def test_version_format():
    assert SEMVER_REGEX.fullmatch(__version__)
