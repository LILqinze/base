from collections import namedtuple


def gen(name):
    return getattr(__import__('networkx.generators'), name)


MODELBASE = namedtuple('ModelBase', ['name', 'gen'])


class Models:
    barabasi_albert_graph = MODELBASE(
        'barabasi_albert_graph', gen('barabasi_albert_graph')
    )
    watts_strogatz_graph = MODELBASE(
        'watts_strogatz_graph', gen('watts_strogatz_graph')
    )
    erdos_renyi_graph = MODELBASE('erdos_renyi_graph', gen('erdos_renyi_graph'))
    fast_gnp_random_graph = MODELBASE(
        'fast_gnp_random_graph', gen('fast_gnp_random_graph')
    )
    gnp_random_graph = MODELBASE('gnp_random_graph', gen('gnp_random_graph'))
    gnm_random_graph = MODELBASE('gnm_random_graph', gen('gnm_random_graph'))
    dense_gnm_random_graph = MODELBASE(
        'dense_gnm_random_graph', gen('dense_gnm_random_graph')
    )
    binomial_graph = MODELBASE('binomial_graph', gen('binomial_graph'))
    newman_watts_strogatz_graph = MODELBASE(
        'newman_watts_strogatz_graph', gen('newman_watts_strogatz_graph')
    )
    connected_watts_strogatz_graph = MODELBASE(
        'connected_watts_strogatz_graph', gen('connected_watts_strogatz_graph')
    )
    random_regular_graph = MODELBASE(
        'random_regular_graph', gen('random_regular_graph')
    )
    extended_barabasi_albert_graph = MODELBASE(
        'extended_barabasi_albert_graph', gen('extended_barabasi_albert_graph')
    )
    powerlaw_cluster_graph = MODELBASE(
        'powerlaw_cluster_graph', gen('powerlaw_cluster_graph')
    )
    random_lobster = MODELBASE('random_lobster', gen('random_lobster'))
    random_shell_graph = MODELBASE('random_shell_graph', gen('random_shell_graph'))
    random_powerlaw_tree = MODELBASE(
        'random_powerlaw_tree', gen('random_powerlaw_tree')
    )
    random_powerlaw_tree_sequence = MODELBASE(
        'random_powerlaw_tree_sequence', gen('random_powerlaw_tree_sequence')
    )
    random_kernel_graph = MODELBASE('random_kernel_graph', gen('random_kernel_graph'))
