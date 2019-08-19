
from setuptools import setup

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='anticipython',
    version='1.0.1',
    description='Create .ics calendars for upcoming CPython releases 🐍👀',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=['anticipython'],
    python_requires='>=3.6',
    url='https://github.com/brcrista/Anticipython',
    author='Brian Cristante',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)