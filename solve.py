from fringe import Stack, Queue, NoRepeatStack, PriorityQueue, Fringe
from successor import successor
from node import Node
from heurisitc import h
import time


def search_solution(init_node: Node, successor, fringe: Fringe, depth_limit: int = 0):
    # h(init_node)
    fringe.add(init_node)
    prev_depth = 0

    while len(fringe.data) > 0:
        candidate_node = fringe.get()
        if candidate_node.depth > prev_depth:
            print(f'finished depth {prev_depth}')
            prev_depth = candidate_node.depth
        if candidate_node.is_goal():
            return candidate_node
        # if depth_limit and candidate_node.depth > depth_limit:
        #     continue
        for el in successor(candidate_node):
            # h(el)
            fringe.add(el)
    return False


def iterative_depth_search_solution(init_node: Node, successor, depth_limit):
    this_round_depth_limit = 1
    f = NoRepeatStack()
    while this_round_depth_limit <= depth_limit:
        result = search_solution(init_node, successor,
                                 f, this_round_depth_limit)
        if result:
            return result
        this_round_depth_limit += 1
    return False


# ===============Testing=============
init_node = Node([[-1, 0, 0, -4], [0, -4, 0, 0],
                  [-2, 0, 0, -3], [0, -3, 0, -1]])
# n = Node([[0 for j in range(15)] for i in range(15)])
f = Stack()
start_time = time.time()
result = search_solution(init_node, successor, f)
# result = iterative_depth_search_solution(init_node, successor, 20)
end_time = time.time()
if not result:
    print('Did not found any solution!')
else:
    for i in range(len(result.state)):
        print(result.state[i])
    print(f"in {end_time - start_time}s")
    #   len(f.data), 'Nodes in general')
