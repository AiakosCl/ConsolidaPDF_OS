from setuptools import setup

APP = ['Consolida_PDF.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyPDF2'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
