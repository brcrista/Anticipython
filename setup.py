from setuptools import setup

# Specify the version here so we can choose to obtain it from environment variables
# later.
VERSION = '1.0.3'

# Specify the description here so we can use UTF-8 characters on all platforms.
DESCRIPTION = "Create .ics calendars for upcoming CPython releases 🐍👀"

# All other settings are read from setup.cfg

setup(
    version=VERSION,
    description=DESCRIPTION,
)
