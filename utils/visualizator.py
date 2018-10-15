import matplotlib.pyplot as plt
import numpy as np
from networkx import draw

from network import MultiLayer


def grid_plot(*args, show=True):
    """Grid plot

    Keyword Arguments:
        *args {tuple} -- args are tuples with (name of graph, plot function without any args)
        show {bool} -- tells whether to draw or not (default: {True})
    """

    size = np.ceil(np.sqrt(len(args)))
    for idx, (name, plot) in enumerate(args):
        plt.subplot(size, size, idx + 1)
        plt.title(name)
        plot()

    if show:
        plt.show()


def plot_2d_data(x, y, x_title, y_title, show=False, title=''):
    assert len(x) == len(y), 'x and y have to be the same length'

    def init_plot(show=False):
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        if title != '':
            plt.title(title)
        plt.plot(x, y)
        if show:
            plt.show()
    if show:
        init_plot(show)
    return init_plot


def plot_network_layers(net):
    assert isinstance(net, MultiLayer), 'Net has to be an instance of MultiLayer'
    from networkx import draw_networkx
    plots = []
    for name, nx_layer in net.layers:
        plots.append((name, lambda: draw(nx_layer)))
    grid_plot(*plots)
