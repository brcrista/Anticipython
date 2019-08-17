import sys

import anticipython
import peps

def main():
    try:
        releases = anticipython.get_release_dates(peps.peps)
        calendar = anticipython.create_ical(releases)
        anticipython.save_ical(calendar, 'cpython_releases.ics')
        return 0
    except Exception as ex:
        print(ex, file=sys.stderr)
        return 1

if __name__ == '__main__':
    exit(main())