import sys

import anticipython
import peps
import peps_store

def main(argv):
    store = peps_store.PepsStore('./.anticipython_peps_store/')
    release_dates = anticipython.get_release_dates(peps.peps, store)
    for version, date in release_dates:
        print(f'{version}: {date}')

if __name__ == '__main__':
    main(sys.argv)