# Cookiecutter templates

This repository contains [Cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for data science projects.

 * [Python - Minimal](./python-minimal/): a simple starting point for a data science project in Python.


## Getting started

First, make sure [Cookiecutter](https://github.com/cookiecutter/cookiecutter) is installed:

```
pip install -U cookiecutter
```

Then, create a project based on a template.
The interactive command line tool will guide you through the selection and configuration of the template.

```
cookiecutter https://github.com/sdsc-innovation/cookiecutter-python.git
```

You can now create an empty repository on GitHub or GitLab (i.e., without an initial README file), and initialize it locally:

```
cd your-project
git init --initial-branch=main
git remote add origin https://github.com/you/your-project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

Please refer to the generated `README.md` for more details, in particular to install dependencies and register pre-commit hooks.
