from node import Node
from copy import deepcopy
from random import randint


def successor(node: Node):
    out_comes = []
    index = [-1, -1]
    size = len(node.state)
    # finding the index of the first 0
    for i in range(size):
        for j in range(size):
            if node.state[i][j] == 0:
                index[0], index[1] = i, j
                break
        if index[0] >= 0:
            break
    # now lets try all the possible outcomes and add the valid ones
    for num in range(size):
        new_node = Node(deepcopy(node.state))
        new_node.state[index[0]][index[1]] = num + 1
        # new_node.state[index[0]][index[1]] = randint(1, size)
        if new_node.is_valid():
            new_node.parent_node = node
            new_node.depth = node.depth + 1
            out_comes.append(new_node)
    return out_comes
