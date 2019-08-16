import sys
from datetime import datetime

import requests

from peps import format_pep_number

def error(message):
    print(message, file=sys.stderr)

def _download(pep_number):
    """
    Fetches PEP files as HTML from python.org.
    """
    # PEP URLs look like https://www.python.org/dev/peps/pep-0123/
    url = f'https://www.python.org/dev/peps/pep-{format_pep_number(pep_number)}/'

    print(f'Downloading PEP {pep_number} ...')
    response = requests.get(url)

    if response.status_code == 200:
        print('Done.')
        return response.text
    else:
        error(f'Could not download {url}. Status code: {response.status_code}')
        return None

def _scrape_releases(pep_html):
    """
    Find the Python versions and their corresponding release dates
    in a PEP for a release schedule.
    """
    yield 'mock-version-1', datetime.now()
    yield 'mock-version-2', datetime.now()

def get_release_dates(peps, peps_store):
    """
    Create a mapping of Python versions to their release dates.
    """
    for version, pep_number in peps.items():
        html = peps_store.load_pep(pep_number)
        if html is None:
            html = _download(pep_number)
            peps_store.store_pep(pep_number, html)
        yield from _scrape_releases(html)