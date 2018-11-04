# Base for experiments with multilayer networks

## Implemented node and edges operations:
  - **specified_layer** - returns a list of nodes from specified layer
  - **available_nodes** - returns a list of nodes aggregated from all layers
  - **edges_on_layers** - returns a list of tuples: (layer_name, edge)
  - **nodes_on_layers** - returns a list of tuples: (layer_name, node)
  - **remove_edge** - removed the edge from the specified layer
  - **remove_node** - removed the node from the specified layer
  - **has_edge** - informs about presence of the edge on the layer

## Implemented measures:
  - **clcc** - cross-layer clustering coefficient
  - **degree** - a degree distributions of every layer
  - **flat_degree** - a degree distribution of all layers

## Implemented transformations:
  - **remove_random_nodes** - removes fraction of nodes from the entire network 
  - **remove_random_edges** - removes fraction of edges from the entire network
  - **rewire_random_edges_preserving_degree** - rewires edges in the entire network
   
## Implemented operations:
  - **rank** - create rank of elements from a network
  - **compare ranks** - compare ranks of elements

## Implemented visualisation:
  - **grid_plot** - plot a grid with specified plots
  - **plot_2d_data** - plot a graph with specified domain and values
  - **plot_network_layers** - plot all layers from passed multilayer

