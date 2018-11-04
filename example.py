#!/usr/bin/env python3
import setup
import networkx.generators as gens
import metrics.cc as cc
import metrics.diagnostic as diag
import metrics.rank as rank
import transformations.destroyer as destroy
from network import Layer, Models, MultiLayer
from pylog import *
from utils import *

example_nets = [
    Layer(Models.watts_strogatz_graph, n=100, p=0.2, k=60),
    Layer(Models.watts_strogatz_graph, n=50, p=0.2, k=30),
]
multilayer = MultiLayer(Layer.combine(*example_nets), *example_nets)

# # GRAPH VISUALIZATION EXAMPLE
# plot_network_layers(multilayer, with_labels=True)

# VISUALIZATION EXAMPLE
plots = []
for idx in range(25):
    example_nets = [
        Layer(Models.watts_strogatz_graph, n=100, p=0.2, k=60),
        Layer(Models.watts_strogatz_graph, n=50, p=0.2, k=30),
    ]
    multilayer = MultiLayer(Layer.combine(*example_nets), *example_nets)
    results = cc.clcc_distribution(multilayer)
    plots.append((f'Some graph #{idx}', plot_2d_data(results[0], results[1], 'Node id', 'CLCC value')))
grid_plot(*plots)

# multilayer = MultiLayer(
#     Layer(Models.watts_strogatz_graph, n=10, p=0.2, k=3),
#     Layer(Models.watts_strogatz_graph, n=5, p=0.2, k=3),
# )

# cc.clcc(multilayer, 1)

# diag.degs_dist(multilayer)
# diag.flat_degs_dist(multilayer)

# destroyer = destroy.Destroyer(multilayer)
# reduced_multilayer = destroyer.remove_random_nodes(0.9)
#
#
# ranking = rank.Rank(multilayer)
# # ranking.calc_rank((diag.flat_degs_dist, True))
# rank_a = ranking.calc_rank(cc.clcc, False)
#
# other_ranking = rank.Rank(reduced_multilayer)
# rank_b = other_ranking.calc_rank(cc.clcc, False)
#
# rank.compare_network_ranks(rank_a, rank_b)
