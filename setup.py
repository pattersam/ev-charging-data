import os
from setuptools import setup

setup(
    name = "ev-charging-data",
    version = "0.0.1",
    author = "Sam Patterson",
    description = "An exploration of the ACN-Data.",
    license = "MIT",
    keywords = "ACN-Data electric-vehicle charging ev",
    url = "https://gitlab.com/s-a-m/ev-charging-data",
    package_dir={'':'src'},
    packages=['ev_charging_data'],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'acnportal',
        'pandas',
        'python-dotenv',
        'SQLAlchemy',
        'typer',
    ],
    entry_points = {
        'console_scripts': ['evcd=ev_charging_data.cli:main'],
    }
)
