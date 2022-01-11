import datetime
import os
import typer

from enum import Enum

from acnportal.acndata import DataClient

import logging
log = logging.getLogger(__name__)

ACN_DATA_API_URL = 'https://ev.caltech.edu/api/v1/'
ACN_DATA_API_TOKEN = os.getenv('ACN_DATA_API_TOKEN')
START_TIME = '2019-05-01T00:00:00+00:00'  # ISO Format
END_TIME = '2019-05-02T00:00:00+00:00'    # ISO Format

class Site(str, Enum):
    caltec = "caltech"
    jpl = "jpl"
    office001 = "office001"


def etl(site: Site, start: str = START_TIME, end: str = END_TIME):
    log.info(f"Getting {site} data from {start} to {end}.")
    client = DataClient(ACN_DATA_API_TOKEN, ACN_DATA_API_URL)

    res = client.get_sessions_by_time(
        site,
        start=datetime.datetime.fromisoformat(start),
        end=datetime.datetime.fromisoformat(end),
    )

    data = list(res)

    log.info(f"{len(data)} rows collected")

def main():
    typer.run(etl)

if __name__ == "__main__":
    main()
