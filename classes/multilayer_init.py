from .layer import Layer
from pylog import *


class MultiLayerInitializer:
    def __init__(self, layers=None):
        if layers:
            self.layer_names = self._layer_names(layers)
            self.layers = self._create_layers(layers)

    def __call__(self, layers=None):
        if layers:
            return self._layer_names(layers), self._create_layers(layers)
        return self.layer_names, self.layers

    def _layer_names(self, layers):
        names = set()
        dbg(f'{__file__}: Setting names', prog=True)
        for idx, layer in enumerate(layers):
            name = f'{idx}_{layer}'
            names.add(name)
            dbg(name)
        ok()
        return names

    def _create_layers(self, layers):
        nx_layers = dict()
        dbg(f'{__file__}: Creating layers', prog=True)
        for layer_name, layer in zip(self.layer_names, layers):
            nx_layers[layer_name] = layer()
        ok()

        return nx_layers
