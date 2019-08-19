# Anticipython

[![PyPI version](https://img.shields.io/pypi/v/anticipython.svg)](https://pypi.org/project/anticipython/)
[![Build status](https://dev.azure.com/briancristante/Anticipython/_apis/build/status/Anticipython?branchName=master)](https://dev.azure.com/briancristante/Anticipython/_build/latest?definitionId=10&branchName=master)

Create .ics calendars for upcoming CPython releases 🐍👀

## Usage

Requires Python 3.6 or later.

```bash
pip install anticipython
python -m anticipython
# Produces an output file named `cpython_releases.ics`
```

### Power user configuration
Edit `peps.py` to include the version and PEPs you want to use.
