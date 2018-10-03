from pylog import *

from .layer import Layer


class MultiLayerInitializer:
    def __init__(self, *layers):
        layers_names = self._layers_names(layers)
        self.layers = self._create_layers(layers_names, layers)

    def __call__(self, layers=None):
        if layers:
            layers_names = self._layers_names(layers)
            return self._create_layers(layers_names, layers)
        return self.layers

    @try_catch_log('Setting names', dbg)
    def _layers_names(self, layers):
        names = set()
        for idx, layer in enumerate(layers):
            name = f'{idx}_{layer}'
            names.add(name)
            dbg(name)
        return names

    @try_catch_log('Creating layers')
    def _create_layers(self, layers_names, layers):
        nx_layers = dict()
        for layer_name, layer in zip(layers_names, layers):
            nx_layers[layer_name] = layer()
            nx_layers[layer_name].name = layer_name
        return nx_layers
