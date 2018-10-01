#!/usr/bin/env python3
import setup
import networkx.generators as gens

import metrics.cc as cc
import metrics.diagnostic as diag
import metrics.rank as rank
from network import Layer, Models, MultiLayer
import transformations.destroyer as destroy

multilayer = MultiLayer(
    Layer(Models.watts_strogatz_graph, n=10, p=0.2, k=3),
    Layer(Models.watts_strogatz_graph, n=5, p=0.2, k=3),
)

diag.degs_dist(multilayer)
diag.flat_degs_dist(multilayer)

cc.clcc(multilayer, 1)

destroyer = destroy.Destroyer(multilayer)
reduced_multilayer = destroyer.destroy_nodes(0.9)

# cc.clcc(reduced_multilayer, 1)

ranking = rank.Rank(multilayer)
ranking.calc_rank((diag.flat_degs_dist, True))
rank_a = ranking.calc_rank((cc.clcc, False))

other_ranking = rank.Rank(reduced_multilayer)
rank_b = other_ranking.calc_rank((cc.clcc, False))

rank.compare_network_ranks(rank_a, rank_b)

rewired_multilayer = destroyer.rewire_edges(10)
