from datetime import datetime

from peps_store import PepsStore

def _download(pep_number):
    """
    Fetches PEP files as HTML from python.org.
    """
    # PEP URLs look like https://www.python.org/dev/peps/pep-0123/
    formatted_pep_number = str(pep_number).rjust(4, '0')
    url = f'https://www.python.org/dev/peps/pep-{formatted_pep_number}/'
    return None

def _scrape_releases(pep_html):
    """
    Find the Python versions and their corresponding release dates
    in a PEP for a release schedule.
    """
    return 'mock-version', datetime.now()

def get_release_dates(peps):
    """
    Create a mapping of Python versions to their release dates.
    """
    peps_store = PepsStore('.anticipython_peps_store')
    for version, pep_number in peps.items():
        html = peps_store.load_pep(pep_number)
        if html is None:
            html = _download(pep_number)
            peps_store.store_pep(pep_number, html)
        yield _scrape_releases(html)