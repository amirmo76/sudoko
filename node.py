class Node:
    parent_node = None
    state = None
    depth = 0
    priority = 0  # the higher the better

    def __init__(self, state):
        self.state = state

    def get_columns(self):
        new_state = []
        for i in range(len(self.state)):
            new_column = []
            for j in range(len(self.state)):
                new_column.append(self.state[j][i])
            new_state.append(new_column)
        return new_state

    def diff(self, node) -> list:
        return [i for i, j in zip(self.state, node.state) if i == j]

    def diff_state(self, state) -> list:
        return [i for i, j in zip(self.state, state) if i == j]

    def is_equal(self, node) -> bool:
        return True if len(self.diff(node)) == len(self.state) else False

    def is_equal_state(self, state) -> bool:
        return True if len(self.diff_state(state)) == len(self.state) else False

    def is_goal(self):
        for row in self.state:
            for num in row:
                if not row.count(num) + row.count(-num) == 1 or num == 0:
                    return False
        for column in self.get_columns():
            for num in column:
                if not column.count(num) + column.count(-num) == 1 or num == 0:
                    return False
        return True

    def is_valid(self):
        for row in self.state:
            for num in row:
                if not row.count(num) + row.count(-num) == 1 and not num == 0:
                    return False
        for column in self.get_columns():
            for num in column:
                if not column.count(num) + column.count(-num) == 1 and not num == 0:
                    return False
        return True

    def __str__(self):
        return "state:" + self.state.__str__() + " ,depth:" + str(self.depth)

    def __repr__(self):
        return self.__str__()
