from node import Node


class Fringe:
    data = list()

    def add(self, node: Node):
        raise NotImplementedError("You haven't implemented this method")

    def get(self):
        raise NotImplementedError("You haven't implemented this method")


class Stack(Fringe):
    def add(self, node: Node):
        self.data.append(node)

    def get(self):
        return self.data.pop()


class Queue(Fringe):
    def add(self, node: Node):
        self.data.append(node)

    def get(self):
        node = self.data[0]
        self.data.remove(node)
        return node


class PriorityQueue(Queue):
    all_time_state = []

    def add(self, node: Node):
        for i in self.all_time_state:
            if node.is_equal_state(i):
                return
        self.all_time_state.append(node.state)
        super().add(node)

    def get(self):
        priority_id = 0
        for i in range(len(self.data)):
            if self.data[i].priority > self.data[priority_id].priority:
                priority_id = i
        node = self.data[priority_id]
        self.data.remove(node)
        return node


class NoRepeatStack(Stack):
    def add(self, node: Node):
        for i in self.data:
            if node.is_equal(i):
                return
        super().add(node)
