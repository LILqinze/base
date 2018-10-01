import copy
import random

import networkx as nx


def reduce_to_frac(elements, frac):
    assert 0 <= frac < 1
    elements = list(elements)
    random.shuffle(elements)
    return elements[:int(frac * len(elements))]


def extract_from_layers(elements_on_layer):
    elements_with_layer = []
    for layer, elements in elements_on_layer:
        for element in elements:
            elements_with_layer.append((layer, element))

    return elements_with_layer


class Destroyer(object):

    def __init__(self, net):
        self._network = net

    def destroy_edges(self, frac):
        edges_to_destroy = reduce_to_frac(extract_from_layers(
            self._network.edges_on_layers()), frac)
        reduced_net = copy.deepcopy(self._network)

        for layer, edge in edges_to_destroy:
            reduced_net.remove_edge(layer, edge)

        return reduced_net

    def destroy_nodes(self, frac):
        nodes_to_destroy = reduce_to_frac(extract_from_layers(
            self._network.nodes_on_layers()), frac)
        reduced_net = copy.deepcopy(self._network)

        for layer, node in nodes_to_destroy:
            reduced_net.remove_node(layer, node)

        return reduced_net

    def rewire_edges(self, layer_tries):
        # TODO: add connected_double_edge_swap in the future :)
        rewired_net = copy.deepcopy(self._network)
        layers_to_rewire = list(rewired_net.layers_names)
        layers_to_rewire = random.choices(layers_to_rewire, k=layer_tries)

        for layer_name in layers_to_rewire:
            nx.double_edge_swap(
                rewired_net.specified_layer(layer_name))

        return rewired_net




