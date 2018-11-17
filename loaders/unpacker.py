import os
from zipfile import ZipFile

from pylog import *
from utils.utils import *

from .datasets import DEFAULT_DATABASE_DIR, KNOWN_ARCHIVE_FORMATS


class Unpacker:

    def __init__(self, dataset_name):
        self._path = f'{DEFAULT_DATABASE_DIR}/{dataset_name}'
        self._dataset_archive_path = self._search_for_database(dataset_name)
        assert file_format(self._dataset_archive_path) in KNOWN_ARCHIVE_FORMATS, 'Unsupported archive format'
        self.unpack_recursive(self._dataset_archive_path)

    def unpack(self, filepath):
        if file_format(filepath) == 'zip':
            return self.unzip(filepath)
        else:
            wrn(f'Not supported file format {filepath}')

    def unpack_recursive(self, filepath):
        to_unpack = set([filepath])
        while to_unpack:
            archive = to_unpack.pop()
            archives_in_archive = self.unpack(archive)
            to_unpack.update(archives_in_archive)
            inf(f'Removing {archive}', prog=True)
            try:
                # os.remove(archive)
                ok()
            except NotImplementedError as e:
                wrn(e)

    @classmethod
    def _search_for_database(cls, filename):
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

