from node import Node


# def h(node: Node):
#     in_place_numbers = 0
#     for num in range(len(node.state[0]) ** 2):
#         goal_index = (((num - 1) // 3), (num - 1) % 3) if num else (2, 2)
#         index = (-1, -1)
#         for row in node.state:
#             try:
#                 index = (node.state.index(row), row.index(num))
#                 if index == goal_index:
#                     in_place_numbers += 1
#             except:
#                 continue
#     node.priority = in_place_numbers


def h(node: Node):
    dist_place_numbers = 0
    for num in range(len(node.state[0]) ** 2):
        goal_index = (((num - 1) // 3), (num - 1) % 3) if num else (2, 2)
        index = (-1, -1)
        for row in node.state:
            try:
                index = (node.state.index(row), row.index(num))
                dist_place_numbers -= abs(goal_index[0] -
                                          index[0]) + abs(goal_index[1] - index[1])
            except:
                continue
    node.priority = dist_place_numbers - node.depth / 2
