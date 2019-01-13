import multiprocessing as mp
from itertools import product, chain
from collections import Counter
from tqdm import tqdm


def clcc(net, node, threshold=1):
    """ Description
    # TODO
    :type net:
    :param net:

    :type node:
    :param node:

    :type threshold:
    :param threshold:

    :raises:

    :rtype:
    """
    lcc_sum = 0.0
    result = lcc_sum
    neighbors_counts = {}

    assert node in net.available_nodes()

    layers = filter(lambda layer: node in layer.nodes(), net.nx_layers)

    neighbors_counts = Counter(chain(*map(lambda layer: layer.neighbors(node), layers)))
    neighbors_counts = {neighbor: occurrences for neighbor, occurrences
                        in neighbors_counts.items() if occurrences >= threshold}
    if not neighbors_counts:
        return result

    neighbors = neighbors_counts.keys()

    for layer, (v, h) in product(net.layers_names, product(neighbors, neighbors)):
        lcc_sum += (net.has_edge(layer, h, v) + net.has_edge(layer, v, h))

    result = lcc_sum / (2 * len(neighbors_counts) * len(net.nx_layers))
    return result


def clcc_distribution(net, treshold=1, njobs=-1, tqdm_enable=True):
    # WRITTEN TO VISUALIZATOR TEST
    # TODO real distribution not only value for each node
    if njobs <= 0:
        njobs = mp.cpu_count()

    all_nodes = list(net.available_nodes())

    with mp.Pool(processes=njobs) as pool:
        results = pool.starmap(clcc, tqdm([[net, node, treshold] for node in all_nodes],
                                          'CLCC',
                                          disable=not tqdm_enable,
                                          leave=False))

    return all_nodes, results
