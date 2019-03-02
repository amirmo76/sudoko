from node import Node
import random
n = Node([[0 for j in range(10)] for i in range(10)])


for row in range(len(n.state)):
    for num in range(len(n.state)):
        n.state[row][num] = random.randint(1, 10)
        while (not n.is_valid()):
            n.state[row][num] = random.randint(1, 10)


for i in range(10):
    print(n.state[i])
