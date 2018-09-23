import networkx as nx

from pylog import *

from .layer import Layer
from .multilayer_init import MultiLayerInitializer

class MultiLayer:
    def __init__(self, *layers):
        initializer = MultiLayerInitializer(layers)
        self._layers = initializer()

    @property
    def layers(self):
        return self._layers.values()

    @property
    def layers_names(self):
        return self._layers.keys()

    def clcc(self, node):
        """Cross-layer clustering coefficient

        Arguments:
            node {integer} : just... node ;-; 
        """
        value = int()
        dbg(f'{__file__} CLCC', True)
        for layer in self._layers.values():
            dbg(layer)
        ok()
        return value
