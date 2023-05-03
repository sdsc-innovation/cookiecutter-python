# Cookiecutter template for Python

...


## Tools

...


## Project structure

...


## Getting started

First, make sure [Cookiecutter](https://github.com/cookiecutter/cookiecutter) is installed:

```
pip install cookiecutter
```

Then, create a project based on this template:

```
cookiecutter https://gitlab.datascience.ch/berdat/cookiecutter-python.git
```


## TODO

 * Finalize pre-commit hooks
   * https://stackoverflow.com/questions/31079047/python-pep8-class-in-init-imported-but-not-used
   * https://pre-commit.com/
 * Improve `cookiecutter.json` and configuration

## Questions

 * `.gitattributes` definitions
 * `.gitignore` definitions
 * `.pre-commit-config.yaml`, specify repo and pin version?
 * Add a `.flake8` file? Or use `setup.cfg`?
 * Black configuration in `pyproject.toml`?
 * Can we also use `pyproject.toml` instead of `setup.py`? In combination with?
 * In order to define a minimal `README.md`, which sections and text should be there?
 * Which Python version, as a minimum?
   * PyTorch requires 3.8
   * NumPy requires 3.9
   * Mac OS on ARM requires 3.9.1 for native execution
 * Should we have `requirements_dev.txt` or not?
 * Which libraries should be in the requirements? Should we pin some versions, and to which values?
 * Do we want to make pre-commit hooks optional (i.e. as an opt-in or opt-out when running cookiecutter)?
 * Should the `src` folder be optional (again, as an opt-in/opt-out)?
 * Is `pip install -e .` the best way to add `src` to the environment, so that notebooks are easy to use?
 * Should we consider some CI/CD, e.g. run tests on GitLab?
 * Conda environment YAML?
 * Better stubs for `src` and `test`?
 * Folder naming convention
 * Already provide command in README to generate documentation? Prepare folders (and stub) accordingly?
 * Should we consider Docker as a template option, or should it be a standalone template?

## References

 * [Python Release Cycle](https://devguide.python.org/versions/#python-release-cycle)
 * [Cookiecutter's documentation](https://cookiecutter.readthedocs.io/)
 * [Cookiecutter template for a Python package](https://github.com/audreyfeldroy/cookiecutter-pypackage)
 * [Cookiecutter template for data science in Python](https://github.com/drivendata/cookiecutter-data-science)
 * https://github.com/sourcery-ai/python-best-practices-cookiecutter
 * https://github.com/cmdoret/renku-project-template/tree/master/python-datasci
 * https://github.com/khuyentran1401/data-science-template
 * [`.gitattributes` best practices](https://rehansaeed.com/gitattributes-best-practices/)
 * https://flake8.pycqa.org/en/latest/user/configuration.html
 * https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file
