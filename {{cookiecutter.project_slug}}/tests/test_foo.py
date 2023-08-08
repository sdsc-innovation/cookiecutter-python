from {{ cookiecutter.module_name }} import bar


def test_bar():
    assert bar() == 42
