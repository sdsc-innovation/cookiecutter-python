# Cookiecutter template for Python

This repository contains a simple Cookiecutter template for Python projects.


## Getting started

First, make sure [Cookiecutter](https://github.com/cookiecutter/cookiecutter) is installed:

```
pip install -U cookiecutter
```

Then, create a project based on this template:

```
cookiecutter https://gitlab.datascience.ch/industry/common/cookiecutter-python.git
```

This will prompt you for:

 1. a project name, used in `README.md`;
 2. a project slug (in `kebab-case`), used for the top-level directory name;
 3. a module name (in `snake_case`);
 4. whether you would like to use Ruff to format and analyze your code;
 5. whether you would like to use pytest to write unit tests.

The module name may also be a short generic identifier, such as `lib` or `helper`, if you do not plan to use it externally.

The generated folder structure is straightforward:

 * code is stored as an installable module, in `src`;
 * unit tests have a dedicated folder in `tests`;
 * notebooks have their own folder;
 * and, by default, a `data` folder is added, as a suggestion.

You can know create an empty repository on GitLab (i.e. without an initial README file), and initialize it locally:

```
cd your-project
git init --initial-branch=main
git remote add origin https://gitlab.datascience.ch/you/your-project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

Apart from adding code, both in `.py` files and notebooks, it is recommended to make sure that dependencies are properly configured. More information about version specifiers can be found in [PEP 440](https://peps.python.org/pep-0440/#version-specifiers).

 * `requirements.txt` should contain the *exact* (a.k.a. pinned) versions of the required dependencies during development. Note that [`pipreqs`](https://github.com/bndr/pipreqs) can be used to infer automatically which packages are used in your code (whereas `pip freeze` would list all installed packages). Also note that `-e .` is used to install your newly created module in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
 * `environment.yml`, by default, delegates to `requirements.txt`.
 * In `pyproject.toml`, under section `tool.poetry.dependencies`, are listed the *install* dependencies of your module. It should represent the minimal versions of the required dependencies during regular usage. Therefore, this typically excludes any development tool, such as `ruff` or `pytest`.

Please refer to the generated `README.md` for more details, in particular to install dependencies and register pre-commit hooks.


## Design choices and tools

 * A `pyproject.toml` file is used instead of `setup.py`, as the latter is deprecated. Also, the TOML file act as a centralized configuration file for other tools.
 * The [`src` layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) is used, to enforce proper use of [editable](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) installation during development.
 * [Poetry](https://python-poetry.org/) is used as build system instead of [PyPA](https://www.pypa.io/en/latest/)'s [Setuptools](https://setuptools.pypa.io/en/latest/), as the configuration syntax is cleaner. However, if you require CPython extensions, you will need to use [Setuptools extension system](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html).
 * `requirements.txt` is used to define development dependencies. An `environment.yml` is also provided for [Conda](http://conda.io) users.
 * [Ruff](https://docs.astral.sh/ruff/) is used for code formatting and linting, using mostly the default configuration.
 * [pytest](https://pytest.org/) is used for unit testing, as the standard `unittest` module tends to be more verbose.
 * [mypy](https://mypy-lang.org/) is suggested for static type checking.
 * [`.gitlab-ci.yml`](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html) is pre-configured to run unit tests on [GitLab CI/CD](https://docs.gitlab.com/ee/ci/).
 * [pre-commit](https://pre-commit.com/) hooks are configured to enforce Ruff, and also some quality-of-life [built-in tools](https://github.com/pre-commit/pre-commit-hooks).


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
 * [Pylint configuration](https://pylint.pycqa.org/en/latest/user_guide/configuration/index.html)
 * [Ruff configuration](https://docs.astral.sh/ruff/configuration/) and [rules](https://docs.astral.sh/ruff/rules/)
 * [Poetry basic usage](https://python-poetry.org/docs/basic-usage/)
 * [Semantic versioning](https://semver.org/)
