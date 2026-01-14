from setuptools import setup, find_packages

setup(
    name="system-log-analyzer",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "log-analyzer=app.main:main"
        ]
    },
    install_requires=[
        "colorama",
        "matplotlib"
    ],
)
