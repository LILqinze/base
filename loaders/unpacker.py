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

    @classmethod
    def _get_all_archives(cls, dirpath):
        assert os.path.isdir(dirpath), f'{dirpath} doesn\'t exist'
        archives = list()
        for root, dirs, files in os.walk(dirpath):
            archive_files = filter(lambda filename: file_format(filename) in KNOWN_ARCHIVE_FORMATS, files)
            archives.extend(map(lambda archive_name: f'{root}/{archive_name}', archive_files))
        return archives

    @classmethod
    def unzip(cls, filepath):
        try:
            inf(f'Unzipping {filepath}', prog=True)
            dirname = filename_without_format(filepath)
            print(dirname)
            exit(0)
            zipfile = ZipFile(filepath, mode='r')
            zipfile.extractall(dirname)
            zipfile.close()
            ok()
            return cls._get_all_archives(filename_from_path(filepath))
        except Exception as e:
            err(e)

