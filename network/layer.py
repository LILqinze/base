import networkx as nx

from .models import ModelBase, Models


class Layer:
    def __init__(self, model, **params):
        assert isinstance(model, ModelBase)

        self._model = model
        self._params = params

    def __call__(self):
        if hasattr(self._model, 'gen'):
            return self._model.gen(**self._params)
        return self._model.model

    def __str__(self):
        return self.name

    @property
    def model(self):
        if hasattr(self._model, 'gen'):
            return self._model.gen
        return self._model.model

    @property
    def params(self):
        return self._params

    @property
    def name(self):
        return self._model.name

    @classmethod
    def combine(cls, *layers, name=None):
        assert len(layers) > 1, 'There has to be more than 1 layer'

        if all(isinstance(layer, Layer) for layer in layers):
            return cls._create_from_layers(name, layers)
        if all(isinstance(layer, nx.Graph) for layer in layers):
            return cls._create_from_nx_graphs(name, layers)

    @classmethod
    def _create_from_nx_graphs(cls, name, layers, directed=False):
        all_edges = set()
        all_nodes = list(range(max(max(layer.nodes for layer in layers))))

        if directed:
            # TODO test whether it works
            all_edges = set.intersection(*list(set(layer.edges) for layer in layers))
        else:
            all_edges = set.intersection(*list(set(reversed(edge)
                                                   for edge in layer.edges).union(layer.edges)
                                               for layer in layers))

        graph = nx.Graph()

        graph.add_nodes_from(all_nodes)
        graph.add_edges_from(all_edges)

        args = {'model': graph}
        if name:
            args['name'] = name
        return Layer(model=Models.combined(**args))

    @classmethod
    def _create_from_layers(cls, name, layers):
        new_layers = list()
        for layer in layers:
            new_layer = layer()
            new_layers.append(new_layer)
        return cls._create_from_nx_graphs(name, new_layers)
