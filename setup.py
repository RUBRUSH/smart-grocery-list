from setuptools import setup, find_packages

setup(
    name="smart-grocery-list",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["smartgrocerylist=app.main:main"],
    },
    author="RUBRUSH",
    author_email="askarsalikov58@gmail.com",
    description="A Python application that automatically generates a grocery list based on user-selected recipes and dietary preferences.",
    license="MIT",
)