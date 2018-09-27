#!/usr/bin/env python3
import setup
import networkx.generators as gens

import metrics.cc as cc
import metrics.diagnostic as diag
from network import Layer, Models, MultiLayer

multilayer = MultiLayer(
    Layer(Models.watts_strogatz_graph, n=10, p=0.2, k=3),
    Layer(Models.watts_strogatz_graph, n=5, p=0.2, k=3),
)

diag.degs_dist(multilayer)
diag.flat_degs_dist(multilayer)

# cc.clcc(multilayer, 1)
