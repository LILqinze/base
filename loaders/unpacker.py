import os
from zipfile import ZipFile

from pylog import *
from utils.utils import file_format

from .datasets import DEFAULT_DATABASE_DIR, KNOWN_ARCHIVE_FORMATS


class Unpacker:

    def __init__(self, dataset_name):
        self._path = f'{DEFAULT_DATABASE_DIR}/{dataset_name}'
        self._dataset_archive_path = self._search_for_dataset(dataset_name)
        assert file_format(self._dataset_archive_path) in KNOWN_ARCHIVE_FORMATS, 'Unsupported archive format'
        
    @staticmethod
    def _search_for_dataset(filename):
        for root, dirs, files in os.walk(DEFAULT_DATABASE_DIR):
            for file in files:
                if filename in file:
                    return f'{root}/{file}'
