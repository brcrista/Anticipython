import datetime
import re

import bs4
import icalendar
import requests

def _format_pep_number(pep_number):
    """
    The PEP number as a 4-digit string.
    This is the format used by the URLs on python.org.
    """
    return str(pep_number).rjust(4, '0')

def _download(pep_number):
    """
    Fetches PEP files as HTML from python.org.
    """
    # PEP URLs look like https://www.python.org/dev/peps/pep-0123/
    url = f'https://www.python.org/dev/peps/pep-{_format_pep_number(pep_number)}/'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise IOError(f'Could not download {url}. Status code: {response.status_code}')

class Release:
    def __init__(self, version, date):
        self.version = version
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')

def _scrape_releases(pep_html):
    """
    Find the Python versions and their corresponding release dates
    in a PEP for a release schedule.
    """
    # As with any scraping, this is a huge hack
    # and very dependent on how the data happens to be formatted.
    soup = bs4.BeautifulSoup(pep_html, features='html.parser')
    for li in soup.find_all('li'):
        # examples of lines we want to match:
        # 3.7.4 final: 2019-07-08
        # 3.8.0 alpha 1: Sunday, 2019-02-03
        match = re.match(r'(\d\.\d\.\d.*)?: (?:\w*, )?(\d\d\d\d-\d\d-\d\d)', li.get_text())
        if match:
            yield Release(version=match.group(1), date=match.group(2))

def get_release_dates(peps):
    """
    Create a sequence of Python versions and their release dates.
    """
    for version, pep_number in peps.items():
        print(f'Downloading PEP {pep_number} ...')
        html = _download(pep_number)
        print('Done.')

        print(f'Scraping PEP {pep_number} for releases ...')
        yield from _scrape_releases(html)
        print('Done.')

def create_ical(releases):
    calendar = icalendar.Calendar()
    # Required to be compliant with RFC 2445
    calendar.add('prodid', '-//Anticipython//https://github.com/brcrista/Anticipython//')
    calendar.add('version', '2.0')

    for release in releases:
        print(f'Adding "{release.version}" to the calendar')
        event = icalendar.Event()
        event.add('summary', f'{release.version} release')
        # Use the DATE type with no DTEND to get an all-day event
        event['dtstart'] = icalendar.prop.vDate(release.date)
        calendar.add_component(event)
    return calendar

def save_ical(calendar, filepath):
    with open(filepath, 'wb') as ical_file:
        ical_file.write(calendar.to_ical())