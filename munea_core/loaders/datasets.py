from collections import namedtuple

__all__ = ['DatabaseElem', 'Database']

DatabaseElem = namedtuple('DatabaseElem', ['name', 'url', 'process_func'])


class Database:
    london_public_transport = DatabaseElem('london_public_transport',
                                           'http://data.dft.gov.uk.s3.amazonaws.com/nptdr/October-2011.zip', 
                                           lambda: None) # TODO parser
