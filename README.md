# Cookiecutter template for Python

...


## Getting started

```
pip install cookiecutter
cookiecutter https://gitlab.datascience.ch/berdat/cookiecutter-python.git
```

You might want to set up `~/.cookiecutterrc`:

```
default_context:
  full_name: "Johan Berdat"
  email: "johan.berdat@epfl.ch"
cookiecutters_dir: "~/.cookiecutters/"
```


## TODO

 * Finalize pre-commit hooks
   * https://stackoverflow.com/questions/31079047/python-pep8-class-in-init-imported-but-not-used
   * https://pre-commit.com/
   * Does it make sense to run tests at each commit? Should probably focus on CI/CD for that
 * Improve `cookicutter.json` and configuration
 * Conda YAML setup


## References

 * [Cookiecutter's documentation](https://cookiecutter.readthedocs.io/)
 * [Cookiecutter template for a Python package](https://github.com/audreyfeldroy/cookiecutter-pypackage)
 * [Cookiecutter template for data science in Python](https://github.com/drivendata/cookiecutter-data-science)
 * https://github.com/sourcery-ai/python-best-practices-cookiecutter
 * [`.gitattributes` best practices](https://rehansaeed.com/gitattributes-best-practices/)
