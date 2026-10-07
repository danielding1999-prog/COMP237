from graph import GRAPH
from collections import deque

# initiate a empty queue
queue = deque([])

# intialite a list to remember visited node
visited = []

# initiate the goal state node
goal = 'Bob'

# intialte the root node
root = 'Daniel'

# current node is the root node
current =""

queue.append(root)
visited.append(root)

tree = {}
index = 0

not_finished = True

list_name = [x for x in GRAPH.keys()] 

if (goal not in list_name):
    print("goal is not in the graph")
    not_finished = False

while (not_finished):

        current = queue.popleft()
        tree[index] = current
        index += 1
        children = GRAPH[current]


        print(f"current: {current}")
        print(f"children: {children}")

        for var in GRAPH[current]:
            if var not in visited:
                queue.append(var)
                visited.append(var)

        print(f"queue: {queue}")

        print("------------------------------------------------------")

        if (current == goal):
            print("goal has been found")
            for index in tree:
                print(f"{index}:{tree[index]}")
            not_finished = False
        

