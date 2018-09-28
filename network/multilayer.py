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

    def available_nodes(self):
        all_nodes = set()
        for layer in self._layers.values():
            all_nodes.update(list(layer.nodes()))
        return all_nodes

    def has_edge(self, layer_name, first_node, second_node):
        return self._layers[layer_name].has_edge(first_node, second_node)
