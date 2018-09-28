from pylog import *

from .layer import Layer


class MultiLayerInitializer:
    def __init__(self, layers):
        self.layers = self._create_layers(layers)

    def __call__(self, layers=None):
        if layers:
            return self._create_layers(layers)
        return self.layers

    def _layers_names(self, layers):
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
        layers_names = self._layers_names(layers)
        dbg(f'{__file__}: Creating layers', prog=True)
        for layer_name, layer in zip(layers_names, layers):
            nx_layers[layer_name] = layer()
            nx_layers[layer_name].name = layer_name
        ok()

        return nx_layers
