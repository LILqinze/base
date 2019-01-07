from munea_core.network import *
from munea_core.metrics import *
from munea_core.transformations import *
from munea_core.utils import *
from munea_core.loaders import *
from .consts import *

import os
for dirname in (DIR_DATASET, ):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
