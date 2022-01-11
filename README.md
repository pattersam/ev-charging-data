# EV Charging Data

Exploration of the the publically available [ACN-Data](https://ev.caltech.edu/dataset).

## Prerequisites

- Python 3 (3.8 has been used for development)

## Installation

- Create a virtual environment using `python -m virtualenv venv`
- Activate the virtual environment using `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/OSX
- Install requirements with `pip install -r requirements.txt`

## Usage

The `evcd` is installed for running the ELT to populate a databse.

For example, to get the data for May 2019 from the `caltech` site, run:

```bash
evcd caltech --start=2019-05-01T00:00:00+00:00 --end=2019-06-01T00:00:00+00:00
```

Run `evcd --help` for more information on it's use.

## Starting the Jupyter Notebook

- Run `jupyter notebook --config=jupyter_notebook_config.py notebooks`

