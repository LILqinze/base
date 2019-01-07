import os
import sys
import time
import urllib.request
from os.path import join as pj

from munea_core.consts import DIR_DATASET
from munea_core.utils import file_format
from pyunpack import Archive

from .datasets import DatabaseElem

__all__ = ['load_database']


def download(dataset_elem: DatabaseElem):
    def reporthook(count, block_size, total_size):
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = min(int(count * block_size * 100 / total_size), 100)
        sys.stdout.write("\rDownloading: %s...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (dataset_elem.name, percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()
    outfile_path = pj(DIR_DATASET, '.'.join([dataset_elem.name,
                                             file_format(dataset_elem.url)]))
    if not os.path.isfile(outfile_path):
        urllib.request.urlretrieve(dataset_elem.url,
                                   outfile_path,
                                   reporthook)


def unpack(dataset_elem: DatabaseElem):
    dir_dataset_path = pj(DIR_DATASET, dataset_elem.name)
    filepath_archive = '.'.join([dir_dataset_path,
                                 file_format(dataset_elem.url)])
    archive = Archive(filepath_archive)
    if not os.path.isdir(dir_dataset_path):
        os.mkdir(dir_dataset_path)

    archive.extractall(dir_dataset_path)
    os.remove(filepath_archive)


def load_database(dataset_elem: DatabaseElem):
    download(dataset_elem)
    unpack(dataset_elem)
