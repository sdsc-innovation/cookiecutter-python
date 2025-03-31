# Cookiecutter template for Python

This template is designed for simple data science project in Python.
It suggests a combination of notebooks and a module for shared utilities.
Development tools are kept to a minimum.


## Getting started

First, make sure [Cookiecutter](https://github.com/cookiecutter/cookiecutter) is installed:

```
pip install -U cookiecutter
```

Then, create a project based on this template:

```
cookiecutter https://github.com/sdsc-innovation/cookiecutter-python.git
```

This will prompt you for:

 * a project name, used in `README.md`;
 * a project slug (in `kebab-case`), used for the top-level directory name;
 * a module name (in `snake_case`);
 * whether you would like to use Ruff to format and analyze your code;
 * whether you would like to use pytest to write unit tests.

The module name may also be a short generic identifier, such as `lib` or `helper`, if you do not plan to use it externally.

The generated folder structure is straightforward:

 * code is stored as an installable module, in `src`;
 * unit tests have a dedicated folder in `tests`;
 * notebooks have their own folder;
 * and, by default, a `data` folder is added, as a suggestion.

You can now create an empty repository on GitHub or GitLab (i.e. without an initial README file), and initialize it locally:

```
cd your-project
git init --initial-branch=main
git remote add origin https://github.com/you/your-project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

Apart from adding code, both in `.py` files and notebooks, it is recommended to make sure that dependencies are properly configured. More information about version specifiers can be found in [PEP 440](https://peps.python.org/pep-0440/#version-specifiers).

 * `requirements.txt` should contain the *exact* (a.k.a. pinned) versions of the required dependencies during development. Note that [`pipreqs`](https://github.com/bndr/pipreqs) can be used to infer automatically which packages are used in your code (whereas `pip freeze` would list all installed packages). Also note that `-e .` is used to install your newly created module in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
 * `environment.yml`, by default, delegates to `requirements.txt`.
 * In `pyproject.toml` are listed the *install* dependencies of your module. It should represent the minimal versions of the required dependencies during regular usage. Therefore, this typically excludes any development tool, such as `ruff` or `pytest`.

If unit tests are enabled during template instantiation, CI/CD configuration files are provided both for GitHub and GitLab. Keep only the one that applies to your scenario.

Please refer to the generated `README.md` for more details, in particular to install dependencies and register pre-commit hooks.


## Design choices and tools

 * Python 3.10 is chosen as a minimum, as 3.9 will reach end-of-life in 2025. We recommend 3.11, as some packages may not fully support 3.12 yet.
 * A [`pyproject.toml`](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) file is the [recommended](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/#is-pyproject-toml-mandatory) way to store configuration.
 * [PyPA](https://www.pypa.io/en/latest/)'s [Setuptools](https://setuptools.pypa.io/en/latest/) is used as build backend, as this is historically the most common solution. However, other options are discussed in [Python Packaging User Guide](https://packaging.python.org/en/latest/), such as [Hatch](https://hatch.pypa.io/latest/) or [Poetry](https://python-poetry.org/).
 * No `setup.py` is provided, as typical projects do not need to access low-level Setuptools configuration. Note that `setup.py` and Setuptools are not [deprecated](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/) as a build backend; [building C extensions](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html) will require this file. 
 * `requirements.txt` is used to define development dependencies. An `environment.yml` is also provided for [Conda](http://conda.io) users. Installation dependencies should be defined in `pyproject.toml`.
 * The [`src` layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) is used, to enforce proper use of [editable](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) installation during development.
 * [Ruff](https://docs.astral.sh/ruff/) is used for code formatting and linting, using mostly the default configuration.
 * [pytest](https://pytest.org/) is used for unit testing, as the standard `unittest` module tends to be more verbose.
 * [mypy](https://mypy-lang.org/) is suggested for static type checking.
 * [`.gitlab-ci.yml`](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html) is pre-configured to run unit tests on [GitLab CI/CD](https://docs.gitlab.com/ee/ci/).
 * [`.github/workflows/pytest.yml`](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) is provided to run unit tests on [GitHub Actions](https://docs.github.com/en/actions).
 * [pre-commit](https://pre-commit.com/) hooks are configured to enforce Ruff, and also some quality-of-life [built-in tools](https://github.com/pre-commit/pre-commit-hooks).
 * No default license file is provided, as this template does not necessarily targets open source projects. By default, copyright applies; [choose a license](https://choosealicense.com/) if you would like to open your project!


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
