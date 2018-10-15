import matplotlib.pyplot as plt
import numpy as np

from network import MultiLayer


def grid_plot(*args, title='', show=True):
    size = np.sqrt(len(args)) + 1
    plt.title(title)
    for idx, plot in enumerate(args):
        plt.subplot(size, size, idx + 1)
        plot()

    if show:

        plt.show()


def plot_2d_data(x, y, x_title, y_title, show=False, title='', **args):
    assert len(x) == len(y), 'x and y have to be the same length'

    def init_plot(show=False):
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.title(title)
        plt.plot(x, y)
        if show:
            plt.show()
    if show:
        init_plot(show)
    return init_plot


def plot_network_layers(net):
    assert isinstance(net, MultiLayer), 'Net has to be an instance of MultiLayer'


    for layer in MultiLayer:
