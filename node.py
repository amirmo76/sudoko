class Node:
    parent_node = None
    state = None
    depth = 0
    priority = 0  # the higher the better

    def __init__(self, state, area: tuple = None):
        self.state = state
        self.area = area

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

    def is_area_valid(self, *state):
        new_state = []
        for row in state:
            for num in row:
                new_state.append(num)
        for num in new_state:
            if not new_state.count(num) + new_state.count(-num) == 1 and not num == 0:
                return False
        return True

    def are_areas_valid(self):
        number_of_areas = len(self.state)**2 // (self.area[0] * self.area[1])
        for i in range(number_of_areas):
            state = []
            for k in range(self.area[1]):
                row = []
                for j in range(self.area[0]):
                    row.append(self.state[k + i // self.area[1] * self.area[1]]
                               [j + (i % self.area[0]) * self.area[0]])
                state.append(row)
            if not self.is_area_valid(*state):
                return False
        return True

    def is_goal(self):
        for row in self.state:
            for num in row:
                if not row.count(num) + row.count(-num) == 1 or num == 0:
                    return False
        for column in self.get_columns():
            for num in column:
                if not column.count(num) + column.count(-num) == 1 or num == 0:
                    return False
        if self.area:
            if not self.are_areas_valid():
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
        if self.area:
            if not self.are_areas_valid():
                return False
        return True

    def __str__(self):
        return "state:" + self.state.__str__() + " ,depth:" + str(self.depth)

    def __repr__(self):
        return self.__str__()
