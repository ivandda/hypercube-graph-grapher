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


cube_dimension = 3
adjacency_list = get_adjacency_list_hypercube(cube_dimension)
print(adjacency_list)
