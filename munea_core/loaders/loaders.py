from .downloader import Downloader
from .unpacker import Unpacker


def load_database(dataset):
    name = dataset[0]
    Downloader(*dataset)()
    Unpacker(name)
