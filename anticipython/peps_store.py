import os

import peps

class PepsStore:
    """
    Local storage for downloaded PEP files.
    Not at all thread-safe.
    """

    def __init__(self, store_path):
        if not os.path.exists(store_path):
            os.mkdir(store_path)
        self._store_path = store_path

    def _get_filepath(self, pep_number):
        formatted_pep_number = peps.format_pep_number(pep_number)
        return os.path.join(self._store_path, f'{formatted_pep_number}.html')

    def store_pep(self, pep_number, contents):
        """
        Store the contents of a file for the given PEP number.
        """
        filepath = self._get_filepath(pep_number)
        with open(filepath, 'w') as f:
            f.write(contents)

    def load_pep(self, pep_number):
        """
        Retrieve the contents of the given PEP if it is in the store,
        or return `None` if it is absent.
        """
        filepath = self._get_filepath(pep_number)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        else:
            return None