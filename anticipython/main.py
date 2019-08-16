import sys

import anticipython
import peps

def main(argv):
    release_dates = anticipython.get_release_dates(peps.peps)
    for version, date in release_dates:
        print(f'{version}: {date}')

if __name__ == '__main__':
    main(sys.argv)