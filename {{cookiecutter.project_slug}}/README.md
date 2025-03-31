# {{ cookiecutter.project_name }}

This project is made using [this template](https://github.com/sdsc-innovation/cookiecutter-python).
Next steps include:

 - [x] Create project from the Cookiecutter template.
 - [ ] Create a virtual environment to work in an isolated Python installation.
 - [ ] Install [pre-commit](https://pre-commit.com/) hooks.
{%- if cookiecutter.use_pytest %}
 - [ ] Keep either `.gitlab-ci.yml` or `.github`, according to your Git hosting platform.
{%- endif %}
 - [ ] Update `authors` and `description`, in `pyproject.toml`.
 - [ ] `requirements.txt` should contain the *exact* (a.k.a. pinned) versions of the dependencies used development, including tools. However, do not include indirect dependencies.
 - [ ] Add installation dependencies in `pyproject.toml`, with permissive version constraints.
 - [ ] Add a `LICENSE` file, if applicable. This is *highly recommended* if the project is open source.
 - [ ] Add a [`CITATION.cff`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), to ease citation of your work.
 - [ ] Replace this `README.md` with a proper one. Among others, it must explain the overall context, the installation instructions, a quick start guide, and a repository structure description.


## Installation

Install pinned development dependencies using:

```
pip install -r requirements.txt
```

If you are using Conda to manage your Python environments:

```
conda env create -f environment.yml
```

Alternatively, if you are using an existing environment, you can install the module in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html), which includes only minimal dependencies:

```
pip install -e .
```


## Development tools

In order to use [pre-commit](https://pre-commit.com/) hooks, they need to be registered:

```
pre-commit install
```

It is a good practice to manually invoke hooks after installation, just in case:

```
pre-commit run --all-files
```
{%- if cookiecutter.use_pytest %}

Unit tests (using [pytest](https://pytest.org/)) are not executed as a pre-commit hook, to keep the overhead to a minimum. Instead, a CI/CD pipeline is configured to run tests after each commit. You can also execute them locally, manually:

```
pytest
```
{%- endif %}

By default, [mypy](https://mypy-lang.org/) is not executed automatically. You can however run them manually:

```
mypy src
```
