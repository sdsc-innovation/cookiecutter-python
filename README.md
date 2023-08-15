# Cookiecutter template for Python

This repository contains a simple Cookiecutter template for Python projects.


## Getting started

First, make sure [Cookiecutter](https://github.com/cookiecutter/cookiecutter) is installed:

```
pip install -U cookiecutter
```

Then, create a project based on this template:

```
cookiecutter https://gitlab.datascience.ch/berdat/cookiecutter-python.git
```

This will prompt you for:

 1. a project name, used in `README.md`;
 2. a project slug, used for the top-level directory name;
 3. a module name;
 4. whether you would like to use Black to format your code;
 5. whether you would like to use pytest to write unit tests.

The module name may also be a short generic identifier, such as `lib` or `helper`, if you do not plan to use it externally.

The generated folder structure is straightforward:

 * code is stored as an installable module, in `src`;
 * unit tests have a dedicated folder in `tests`;
 * notebooks have their own folder;
 * and, by default, a `data` folder is added, as a suggestion.

Apart from adding code, both in `.py` files and notebooks, it is recommended to make sure that dependencies are properly configured:

 * `requirements.txt` should contain the *exact* (a.k.a. pinned) versions of the required dependencies during development. Note that[`pipreqs`](https://github.com/bndr/pipreqs) can be used to infer automatically which packages are used in your code (whereas `pip freeze` would list all installed packages). Note that `-e .` is used to install your newly created module in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
 * `environment.yml`, by default, delegates to `requirements.txt`.
 * In `pyproject.toml`, under section `tool.poetry.dependencies`, are listed the *install* dependencies of your module. It should represent the minimal versions of the required dependencies during regular usage. Therefore, this typically excludes any development tool, such as `pylint` or `pytest`.

Please refer to the generated `README.md` for more details, in particular to install dependencies and register pre-commit hooks.


## Design choices and tools

 * A `pyproject.toml` file is used instead of `setup.py`, as the latter is deprecated. Also, the TOML file act as a centralized configuration file for other tools.
 * The [`src` layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) is used, to enforce proper use of [editable](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) installation during development.
 * [Poetry](https://python-poetry.org/) is used as build system instead of [PyPA](https://www.pypa.io/en/latest/)'s [Setuptools](https://setuptools.pypa.io/en/latest/), as the configuration syntax is cleaner. However, if you require CPython extensions, you will need to use [Setuptools extension system](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html).
 * `requirements.txt` is used to define development dependencies. An `environment.yml` is also provided for [Conda](http://conda.io) users.
 * [Black](https://black.readthedocs.io/en/stable/) is used for code formatting, using the default configuration.
 * [pytest](https://pytest.org/) is used for unit testing, as the standard `unittest` module tends to be more verbose.
 * [mypy](https://mypy-lang.org/) is suggested for static type checking.
 * [pylint](https://www.pylint.org/) is suggested for static code analysis.
 * [`.gitlab-ci.yml`](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html) is pre-configured to run unit tests on [GitLab CI/CD](https://docs.gitlab.com/ee/ci/).
 * [pre-commit](https://pre-commit.com/) hooks are configured to enforce Black, and also some quality-of-life [built-in tools](https://github.com/pre-commit/pre-commit-hooks).


## References

 * [Python Release Cycle](https://devguide.python.org/versions/#python-release-cycle)
 * [Cookiecutter](https://cookiecutter.readthedocs.io/) templates:
    * https://github.com/audreyfeldroy/cookiecutter-pypackage
    * https://github.com/drivendata/cookiecutter-data-science
    * https://github.com/sourcery-ai/python-best-practices-cookiecutter
    * https://github.com/SwissDataScienceCenter/renku-project-template/tree/master/python-minimal
    * https://github.com/cmdoret/renku-project-template/tree/master/python-datasci
    * https://github.com/khuyentran1401/data-science-template
 * [`.gitattributes` best practices](https://rehansaeed.com/gitattributes-best-practices/)
 * [Flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html)
 * [Black configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)
 * [Poetry basic usage](https://python-poetry.org/docs/basic-usage/)
