import networkx as nx
from networkx import MultiDiGraph

from pylog import *

from .layer import Layer


class MultiLayer:
    def __init__(self, *layers):
        self._graph = self._create_graph(layers)

    def __del__(self):
        pass

    def _create_graph(self, layers):
        # TODO
        raise NotImplementedError

        if all(isinstance(layer, Layer) for layer in layers):
            nx_layers = list(map(lambda x: x(), layers))
            layers = list(layer.name for layer in layers)
        elif all(isinstance(layer, nx.Graph) for layer in layers):
            nx_layers = layers
            layers = range(len(nx_layers))
        else:
            raise AttributeError(
                'layers must be objects of nx.Graph or derivatives or Layer'
            )

        graph = MultiDiGraph()

        for idx, layer in enumerate(zip(nx_layers, layers)):
            inf(layer[0].nodes)
            layer_name = f'{idx}_{layer[1]}'
            graph.add_nodes_from(layer[0].nodes, name=layer_name)
            graph.add_edges_from(layer[0].edges, name=layer_name)

        inf(graph.adj)
        return None

    @property
    def graph(self):
        return self._graph
