import os
import shutil
import sys


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


REMOVED_PATHS = [
    # {% if not cookiecutter.use_pytest %}
    "tests",
    ".gitlab-ci.yml",
    # {% endif %}
]


for path in REMOVED_PATHS:
    path = path.strip()
    if path:
        remove(path)
