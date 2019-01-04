from collections import namedtuple


def gen(name):
    return getattr(__import__('networkx.generators'), name)


class ModelBase:
    def __init__(self, name, gen=None, model=None):
        assert not bool(gen) != (not bool(model)), 'There has to be only one of (gen, model)'
        self.name = name
        if gen:
            self.gen = gen
        else:
            self.model = model


class Models:

    # NETWORKX GRAHPS
    barabasi_albert_graph          = ModelBase(name='barabasi_albert_graph', gen=gen('barabasi_albert_graph'))
    watts_strogatz_graph           = ModelBase(name='watts_strogatz_graph', gen=gen('watts_strogatz_graph'))
    erdos_renyi_graph              = ModelBase(name='erdos_renyi_graph', gen=gen('erdos_renyi_graph'))
    fast_gnp_random_graph          = ModelBase(name='fast_gnp_random_graph', gen=gen('fast_gnp_random_graph'))
    gnp_random_graph               = ModelBase(name='gnp_random_graph', gen=gen('gnp_random_graph'))
    gnm_random_graph               = ModelBase(name='gnm_random_graph', gen=gen('gnm_random_graph'))
    dense_gnm_random_graph         = ModelBase(name='dense_gnm_random_graph', gen=gen('dense_gnm_random_graph'))
    binomial_graph                 = ModelBase(name='binomial_graph', gen=gen('binomial_graph'))
    newman_watts_strogatz_graph    = ModelBase(name='newman_watts_strogatz_graph', gen=gen('newman_watts_strogatz_graph'))
    connected_watts_strogatz_graph = ModelBase(name='connected_watts_strogatz_graph', gen=gen('connected_watts_strogatz_graph'))
    random_regular_graph           = ModelBase(name='random_regular_graph', gen=gen('random_regular_graph'))
    extended_barabasi_albert_graph = ModelBase(name='extended_barabasi_albert_graph', gen=gen('extended_barabasi_albert_graph'))
    powerlaw_cluster_graph         = ModelBase(name='powerlaw_cluster_graph', gen=gen('powerlaw_cluster_graph'))
    random_lobster                 = ModelBase(name='random_lobster', gen=gen('random_lobster'))
    random_shell_graph             = ModelBase(name='random_shell_graph', gen=gen('random_shell_graph'))
    random_powerlaw_tree           = ModelBase(name='random_powerlaw_tree', gen=gen('random_powerlaw_tree'))
    random_powerlaw_tree_sequence  = ModelBase(name='random_powerlaw_tree_sequence', gen=gen('random_powerlaw_tree_sequence'))
    random_kernel_graph            = ModelBase(name='random_kernel_graph', gen=gen('random_kernel_graph'))

    #CUSTOM GRAPHS
    combined = lambda model, name='combined': ModelBase(name=name, model=model)
