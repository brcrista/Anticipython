"""
Maps major.minor versions to the PEP number detailing the release schedule for that version.
"""

peps = {
    '3.6': 494,
    '3.7': 537,
    '3.8': 569
}

def format_pep_number(pep_number):
    """
    The PEP number as a 4-digit string.
    This is the format used by the URLs on python.org.
    """
    return str(pep_number).rjust(4, '0')