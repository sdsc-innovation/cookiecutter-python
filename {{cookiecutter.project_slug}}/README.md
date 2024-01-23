# {{ cookiecutter.project_name }}

...


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

Unit tests (using [pytest](https://pytest.org/)) are not executed as a pre-commit hook, to keep the overhead to a minimum. Instead, assuming that GitLab CI/CD is available, a `.gitlab-ci.yml` is configured to run tests after each commit. You can also execute them locally, manually:

```
pytest
```
{%- endif %}

By default, [mypy](https://mypy-lang.org/) is not executed automatically. You can however run them manually:

```
mypy src
```
