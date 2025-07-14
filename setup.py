from setuptools import setup, find_packages

setup(
    name="nosqli-bruter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
    ],
    entry_points={
    'console_scripts': [
        'nosqli-bruter = bruter.main:cli_entry',
        ],
    },
    author="sherlockteen",
    description="NoSQL Injection Brute Forcer | Red Team Tool",
    url="https://github.com/sherlockteen/nosqli-bruter",
)
