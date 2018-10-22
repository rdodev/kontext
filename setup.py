# Ruben Orduz (c) 2018
from setuptools import setup

setup(
    name='kontext',
    version='0.0.2',
    py_modules=['kontext'],
    include_package_data=True,
    entry_points=
    """
    [console_scripts]
    kontext=kontext:kontext
    """,
)