import kglab

namespaces = {
    "ex": "http://example.com/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}

kg = kglab.KnowledgeGraph(name="A KG example", namespaces=namespaces)

kg.materialize("morph_configs/main_config.ini")

kg.load_rdf("data/artefacts.ttl")

# Define a dictionary called VIS_STYLE that specifies visualization styles for different types of nodes in the graph
VIS_STYLE = {
    "owl": {
        "color": "orange",
        "size": 20,
    },
    "ex": {
        "color": "blue",
        "size": 35,
    },
}

# Create a SubgraphTensor object from the knowledge graph, which allows for tensor-based operations on the graph
subgraph = kglab.SubgraphTensor(kg)

# Build a PyVis graph object from the SubgraphTensor, specifying that it should be rendered in a Jupyter notebook and using the VIS_STYLE dictionary for node styling
pyvis_graph = subgraph.build_pyvis_graph(notebook=True, style=VIS_STYLE)

# Apply a force-directed graph layout algorithm (Force Atlas 2) to the PyVis graph
pyvis_graph.force_atlas_2based()

# Save the PyVis graph as an HTML file
pyvis_graph.show("output/graph.html")

# Save the knowledge graph as a TTL (Turtle) file
kg.save_rdf("output/data.ttl")

# Convert triples to string and print
ttl = kg.save_rdf_text()
print(ttl)
