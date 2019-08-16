class PepsStore:
    """
    Local storage for downloaded PEP files.
    Not at all thread-safe.
    """

    def __init__(self, store_path):
        self._store_path = store_path

    def store_pep(self, pep_number, contents):
        """
        Store the contents of a file for the given PEP number.
        """
        pass

    def load_pep(self, pep_number):
        """
        Retrieve the contents of the given PEP if it is in the store,
        or return `None` if it is absent.
        """
        return None