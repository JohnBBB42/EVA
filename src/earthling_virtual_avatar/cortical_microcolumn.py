# %% [code]
import networkx as nx
import matplotlib.pyplot as plt
import random
import math

# Set random seed for reproducibility
random.seed(42)

# Create a directed graph to represent the minicolumn
G = nx.DiGraph()

# Define the layers and assign neuron counts per layer (simplified distribution)
layers = {
    'Layer I': 5,      # very few neurons (mostly neuropil)
    'Layer II/III': 40,
    'Layer IV': 20,    # primary input layer in sensory areas
    'Layer V': 25,     # output to subcortical targets
    'Layer VI': 10     # additional output layer
}

neuron_info = {}  # will store neuron id -> (layer, type)
layer_neurons = {}  # mapping from layer name to list of neuron ids

# Create neurons with an id and assign type (80% excitatory, 20% inhibitory)
neuron_id = 0
for layer, count in layers.items():
    layer_neurons[layer] = []
    for _ in range(count):
        neuron_type = 'excitatory' if random.random() < 0.8 else 'inhibitory'
        G.add_node(neuron_id, layer=layer, neuron_type=neuron_type)
        neuron_info[neuron_id] = (layer, neuron_type)
        layer_neurons[layer].append(neuron_id)
        neuron_id += 1

# Define connection probabilities (arbitrary illustrative values)
p_intra_excitatory = 0.1  # intra-layer excitatory-to-excitatory
p_intra_inhibitory = 0.3  # connections involving inhibitory neurons within same layer
p_inter = 0.3           # inter-layer (feedforward) probability

# Add intra-layer connections (within the same layer)
for layer, neurons in layer_neurons.items():
    for i in neurons:
        for j in neurons:
            if i != j:
                # Use a higher probability if one neuron is inhibitory
                if G.nodes[i]['neuron_type'] == 'inhibitory' or G.nodes[j]['neuron_type'] == 'inhibitory':
                    prob = p_intra_inhibitory
                else:
                    prob = p_intra_excitatory
                if random.random() < prob:
                    G.add_edge(i, j)

# Function to add inter-layer connections with a given probability
def add_inter_layer_connections(source_layer, target_layer, prob):
    for i in layer_neurons[source_layer]:
        for j in layer_neurons[target_layer]:
            if random.random() < prob:
                G.add_edge(i, j)

# Add feedforward connections
add_inter_layer_connections('Layer IV', 'Layer II/III', p_inter)
add_inter_layer_connections('Layer II/III', 'Layer V', p_inter)
add_inter_layer_connections('Layer V', 'Layer VI', p_inter)
# Optionally, add a feedback connection
add_inter_layer_connections('Layer V', 'Layer II/III', 0.1)

# Assign a random weight to each edge (if not already assigned)
for u, v in G.edges():
    if 'weight' not in G[u][v]:
        # For simplicity, weights are chosen between 0.5 and 1.5
        G[u][v]['weight'] = random.uniform(0.5, 1.5)

# Visualization of the network (arranged by layer)
pos = {}
y_values = {
    'Layer I': 5,
    'Layer II/III': 4,
    'Layer IV': 3,
    'Layer V': 2,
    'Layer VI': 1
}
for layer, neurons in layer_neurons.items():
    x_positions = [i for i in range(len(neurons))]
    for idx, neuron in enumerate(neurons):
        pos[neuron] = (x_positions[idx], y_values[layer])

# Plot graph for visual explanation
#plt.figure(figsize=(12, 6))
#nx.draw(G, pos, node_size=300,
#        node_color=['skyblue' if G.nodes[n]['neuron_type'] == 'excitatory' else 'salmon'
#                    for n in G.nodes],
#        arrowsize=8, with_labels=True)
#plt.title("Simplified Model of a Cortical Minicolumn")
#plt.axis('off')
#plt.show()

# %% [markdown]
# ### Network Simulation: Taking Input and Producing Output
#
# In the simulation below:
# - We “clamp” the input layer (default: **Layer IV**) to a given input value.
# - Each neuron updates its activation based on the weighted sum of its incoming neighbors using the `tanh` activation function.
# - The input neurons are re-clamped at every time step.
# - After a fixed number of time steps, activations of neurons in specified output layers (default: **Layer V** and **Layer VI**) are returned.

# %% [code]
def simulate_network(graph, layer_neurons, input_layer='Layer IV', 
                     input_value=1.0, output_layers=['Layer V', 'Layer VI'], 
                     steps=10, clamp_input=True):
    """
    Simulate network dynamics:
      - 'graph': the NetworkX DiGraph.
      - 'layer_neurons': dictionary mapping layer names to list of neuron ids.
      - 'input_layer': name of the input layer to clamp to input_value.
      - 'input_value': value to assign to neurons in the input layer.
      - 'output_layers': list of layer names from which to collect outputs.
      - 'steps': number of simulation time steps.
      - 'clamp_input': if True, the input layer is reset to input_value at every step.
      
    Returns:
      - A dictionary mapping neuron id (in output layers) to its final activation.
    """
    # Initialize all neuron activations to 0.
    activations = {node: 0.0 for node in graph.nodes()}
    
    # Clamp the input layer neurons to the input_value
    for node in layer_neurons[input_layer]:
        activations[node] = input_value
    
    # Run the simulation for a fixed number of time steps
    for step in range(steps):
        new_activations = {}
        for node in graph.nodes():
            # Sum the weighted activations from all incoming neurons
            total_input = 0.0
            for pred in graph.predecessors(node):
                weight = graph[pred][node]['weight']
                total_input += activations[pred] * weight
            # Update using the tanh activation function
            new_activations[node] = math.tanh(total_input)
        
        # If clamping, reassign the input neurons to input_value after update.
        if clamp_input:
            for node in layer_neurons[input_layer]:
                new_activations[node] = input_value
        activations = new_activations
    
    # Gather output activations from the specified output layers.
    output_activations = {}
    for layer in output_layers:
        for node in layer_neurons[layer]:
            output_activations[node] = activations[node]
    
    return output_activations

# Run the simulation with external input on Layer IV
output_results = simulate_network(G, layer_neurons, input_layer='Layer IV', 
                                  input_value=1.0, output_layers=['Layer V', 'Layer VI'], 
                                  steps=15, clamp_input=True)

print("Output activations from designated output layers:")
for node, act in output_results.items():
    layer = G.nodes[node]['layer']
    ntype = G.nodes[node]['neuron_type']
    print(f"Neuron {node} in {layer} ({ntype}): {act:.3f}")
