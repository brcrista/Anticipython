import sys

from anticipython import anticipython, peps

def main():
    try:
        releases = anticipython.get_release_dates(peps.peps)
        calendar = anticipython.create_ical(releases)

        output_file = 'cpython_releases.ics'
        print(f'Writing output to {output_file} ...')
        anticipython.save_ical(calendar, output_file)
        print('Done.')
        return 0
    except Exception as ex:
        print(ex, file=sys.stderr)
        return 1

if __name__ == '__main__':
    exit(main())