"""
Use setup tools to setup the armory has a standard python module
"""
from setuptools import setup, find_packages


setup(
    name="baidu",
    version="0.0.1",
    description="Reusable scrapes/test cases for the baidu codebase",
    url="https://github.com/jessicawjr/berry",
    packages=find_packages(),
    install_requires=[
        'selenium==2.52.0',
        'requests',
        'pyvirtualdisplay',
        'google-api-python-client==1.5.0',
        'beautifulsoup4',
        'easyprocess',
        'pyyaml',
        'mysqlclient',
        'retry',
    ],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "baidu=baidu.cli:main",
        ]
    },
)
