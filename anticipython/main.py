import sys

import anticipython
import peps

def main():
    try:
        release_dates = anticipython.get_release_dates(peps.peps)
        for version, date in release_dates:
            print(f'{version}: {date}')
        return 0
    except Exception as ex:
        print(ex, file=sys.stderr)
        return 1

if __name__ == '__main__':
    exit(main())