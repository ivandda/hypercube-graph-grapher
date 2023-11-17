import matplotlib.pyplot as plt
import networkx as nx


def get_adjacency_list_hypercube(n):
    all_nodes = get_all_nodes(n)
    all_nodes_adjacencies = {node: [] for node in all_nodes}

    for node_index, node in enumerate(all_nodes):
        for next_node_index in range(node_index + 1, len(all_nodes)):
            if get_node_binary_difference(node, all_nodes[next_node_index]) == 1:
                all_nodes_adjacencies[node].append(all_nodes[next_node_index])
                all_nodes_adjacencies[all_nodes[next_node_index]].append(node)

    return all_nodes_adjacencies


def get_all_nodes(cube_dimension):
    if cube_dimension == 0:
        raise ValueError('The dimension of the hypercube must be greater than 0')
    nodes = ['']
    for i in range(cube_dimension):
        nodes = ['0' + s for s in nodes] + ['1' + s for s in nodes]
    return nodes


def get_node_binary_difference(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def plot_hypercube_graph(n, adjacency):
    G = nx.Graph(adjacency)
    pos = nx.circular_layout(G)
    plt.figure(figsize=(8, 6))

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')

    # Number of vertices and edges
    num_vertices = 2 ** n
    num_edges = n * (2 ** (n - 1))

    plt.text(0.05, 0.95, f"Number of Vertices: {num_vertices}", ha='left', va='center', fontsize=10,
             transform=plt.gca().transAxes)
    plt.text(0.05, 0.90, f"Number of Edges: {num_edges}", ha='left', va='center', fontsize=10,
             transform=plt.gca().transAxes)

    plt.title(f'Hypercube Graph of {n} dimensions')
    plt.savefig(f'hypercube_{n}_dimensions.png')  # Save the plot as an image file
    plt.show()
    plt.close()


def main():
    # cube_dimension = 4
    cube_dimension = int(input("Enter the dimension of the hypercube: "))
    adjacency_list = get_adjacency_list_hypercube(cube_dimension)
    print(adjacency_list)
    plot_hypercube_graph(cube_dimension, adjacency_list)


if __name__ == '__main__':
    main()
