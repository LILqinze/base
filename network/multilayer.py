import networkx as nx

from pylog import *

from .layer import Layer
from .multilayer_init import MultiLayerInitializer


class MultiLayer:
    def __init__(self, *layers):
        initializer = MultiLayerInitializer(layers)
        self._layers = initializer()

    @property
    def nx_layers(self):
        return self._layers.values()

    @property
    def layers_names(self):
        return self._layers.keys()

    @property
    def layers(self):
        return self._layers.items()

