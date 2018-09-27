from pylog import *


def clcc(net, node):
    """Cross-layer clustering coefficient

    Arguments:
        node {integer} : just... node ;-;
    """
    value = int()
    dbg(f'{__file__} CLCC', True)
    for layer in net.nx_layers:
        dbg(layer)
    ok()
    return value


def lcc_brodka(net, node, threshold=1):
    """
    :param net:
    :param node:
    :param threshold:
    :return:
    """
    lcc_sum = 0
    neighbors_counts = {}
    layers = net.nx_layers

    for layer in layers:
        for neighbor in layer.neighbors(node):
            neighbors_counts[neighbor] = neighbors_counts.get(neighbor, 0) + 1

    neighbors_counts = {neighbor: occurrences for neighbor, occurrences
                        in neighbors_counts.items() if occurrences >= threshold}

    if not neighbors_counts:
        return 0

    for layer in net.layers_names:
        for v in neighbors_counts.keys():
            for h in neighbors_counts.keys():
                lcc_sum += (net.has_edge(layer, h, v) + net.has_edge(layer, v, h))

    return lcc_sum / (2 * len(neighbors_counts) * len(layers))
