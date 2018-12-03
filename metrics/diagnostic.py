

def degs_dist(net):
    """
    :param net: a multilayer network
    :return: a dict with distribution of node degrees (for each layer)
    """
    dist = {}
    for layer_name, layer in net.layers:
        for node in layer.nodes():
            degree_key = (layer_name, layer.degree(node))
            dist[degree_key] = dist.get(degree_key, 0) + 1
    return dist


def flat_degs_dist(net):
    """
    :param net: a multilayer network
    :return: a dict with distribution of node degrees (a sum from each layer)
    """
    dist = degs_dist(net)
    flat_dist = {}
    for dist_key in dist.keys():
        _, degree = dist_key
        flat_dist[degree] = flat_dist.get(degree, 0) + dist[dist_key]

    return flat_dist
