from collections import namedtuple


def gen(name):
    return getattr(__import__('networkx.generators'), name)


ModelBase = namedtuple('ModelBase', ['name', 'gen'])


class Models:
    barabasi_albert_graph = ModelBase(
        'barabasi_albert_graph', gen('barabasi_albert_graph')
    )
    watts_strogatz_graph = ModelBase(
        'watts_strogatz_graph', gen('watts_strogatz_graph')
    )
    erdos_renyi_graph = ModelBase('erdos_renyi_graph', gen('erdos_renyi_graph'))
    fast_gnp_random_graph = ModelBase(
        'fast_gnp_random_graph', gen('fast_gnp_random_graph')
    )
    gnp_random_graph = ModelBase('gnp_random_graph', gen('gnp_random_graph'))
    gnm_random_graph = ModelBase('gnm_random_graph', gen('gnm_random_graph'))
    dense_gnm_random_graph = ModelBase(
        'dense_gnm_random_graph', gen('dense_gnm_random_graph')
    )
    binomial_graph = ModelBase('binomial_graph', gen('binomial_graph'))
    newman_watts_strogatz_graph = ModelBase(
        'newman_watts_strogatz_graph', gen('newman_watts_strogatz_graph')
    )
    connected_watts_strogatz_graph = ModelBase(
        'connected_watts_strogatz_graph', gen('connected_watts_strogatz_graph')
    )
    random_regular_graph = ModelBase(
        'random_regular_graph', gen('random_regular_graph')
    )
    extended_barabasi_albert_graph = ModelBase(
        'extended_barabasi_albert_graph', gen('extended_barabasi_albert_graph')
    )
    powerlaw_cluster_graph = ModelBase(
        'powerlaw_cluster_graph', gen('powerlaw_cluster_graph')
    )
    random_lobster = ModelBase('random_lobster', gen('random_lobster'))
    random_shell_graph = ModelBase('random_shell_graph', gen('random_shell_graph'))
    random_powerlaw_tree = ModelBase(
        'random_powerlaw_tree', gen('random_powerlaw_tree')
    )
    random_powerlaw_tree_sequence = ModelBase(
        'random_powerlaw_tree_sequence', gen('random_powerlaw_tree_sequence')
    )
    random_kernel_graph = ModelBase('random_kernel_graph', gen('random_kernel_graph'))
