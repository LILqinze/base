# Base for experiments with multilayer networks

## Implemented node and edges operations:
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
  - **destroy_nodes** - removes fraction of nodes from the entire network 
  - **destroy_edges** - removes fraction of edges from the entire network
  - **rewire_edges** - rewires edges in the entire network
   
## Implemented operations:
  - **rank** - create rank of elements from a network
  - **compare ranks** - compare ranks of elements
