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
