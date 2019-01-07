import os

import requests as reqs
from tqdm import tqdm

from utils.utils import file_format

from .datasets import DEFAULT_DATABASE_DIR


class Downloader:
    def __init__(self, name, url):
        self._name = name
        self._url = url

    def __call__(self):
        format = file_format(self._url)
        filepath = f'{DEFAULT_DATABASE_DIR}/{self._name}'
        if os.path.isdir(filepath) or os.path.isfile(f'{filepath}.{format}'):
            wrn(f'{filepath} already exists. Skipping downloading.')
            return
        try:
            self._create_database_dir_if_not_exists()
            inf(f'{self._name} database to be downloaded from {self._url}')
            response = reqs.get(self._url, stream=True)
            file_size = int(response.headers['Content-Length'])
            chunk_no, chunk_size = 1, 1024
            num_bars = int(file_size / chunk_size)
            with open(f'{filepath}.{format}', 'wb') as fp:
                for chunk_no in tqdm(response.iter_content(chunk_size=chunk_size),
                                     total=num_bars,
                                     unit='KB',
                                     desc=f'Downloading {self._name}',
                                     leave=True):
                    fp.write(chunk_no)
            inf(f'Saved to {filepath}.{format}')
        except Exception as e:
            err(e)

    def _create_database_dir_if_not_exists(self):
        if not os.path.isdir(DEFAULT_DATABASE_DIR):
            inf(f'Creating database directory in {DEFAULT_DATABASE_DIR}')
            os.mkdir(DEFAULT_DATABASE_DIR)
