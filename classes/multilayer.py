import networkx as nx
from networkx import MultiDiGraph

from pylog import *

from .layer import Layer
from .multilayer_init import MultiLayerInitializer


class MultiLayer:
    def __init__(self, *layers):
        initializer = MultiLayerInitializer()
        self._layers_names, self._layers = initializer(layers)

    @property
    def layers(self):
        return self._layers

    @property
    def layers_names(self):
        return self._layers_names
