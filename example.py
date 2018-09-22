#!/usr/bin/env python3
import setup
import networkx.generators as gens

from classes import Layer, Models, MultiLayer

multilayer = MultiLayer(
    Layer(Models.watts_strogatz_graph, n=10, p=0.2, k=3),
    Layer(Models.watts_strogatz_graph, n=5, p=0.2, k=3),
)

