import random

class Node:

    def __init__(self, state=None, length=None, from_node=None, heur=None):
        self.state = state         # `list` of numbers from 0 to 8
        self.length = length             # `int` how far from start the current state
        self.from_node = from_node # `Node` from which come
        self.heur = heur           # `int` approximate distance to the goal state

    @property
    def full(self):
        return self.length + self.heur # `int` sum of len and heur

def get_heur(from_state, to_state):
    heur = 0
    for i in range(len(from_state)):
        for j in range(len(from_state[i])):
            if from_state[i][j] != 0 and from_state[i][j] == to_state[i][j]:
                heur += 1
    return heur

def get_result(node):
    state_list = []
    current_node = node
    while(current_node != None):
        state_list.append(current_node.state)
        current_node = current_node.from_node
    state_list.reverse()
    return state_list

def get_neighbors(current_node, goal_state):
    neighbour_nodes, neighbour_states = [], []

    for i in range(len(current_node.state)):
        for j in range(len(current_node.state[i])):
            if current_node.state[i][j] == 0:
                if i + 1 < 3:
                    neighbour_states.append(swap(current_node.state, [i, j], [i + 1, j]))
                if i - 1 > -1:
                    neighbour_states.append(swap(current_node.state, [i, j], [i - 1, j]))
                if j + 1 < 3:
                    neighbour_states.append(swap(current_node.state, [i, j], [i, j + 1]))
                if j - 1 > -1:
                    neighbour_states.append(swap(current_node.state, [i, j], [i, j - 1]))

    for neighbour_state in neighbour_states:
        neighbour_nodes.append(Node(
            state=neighbour_state,
            length=current_node.length + 1,
            from_node=current_node,
            heur=get_heur(neighbour_state, goal_state)
        ))
    return neighbour_nodes

def swap(s, a, b):
    state = list(s)
    temp = state[a[0]][a[1]]
    state[a[0]][a[1]] = state[b[0]][b[1]]
    state[b[0]][b[1]] = temp
    return state

def find_path(start_state, goal_state):

    closed_set, open_set = [], []

    num = 20

    start_node = Node(
        state=start_state,
        length=0,
        from_node=None,
        heur=get_heur(start_state, goal_state)
    )

    open_set.append(start_node)

    while(len(open_set) > 0):

        current_node = sorted(open_set, key=lambda node: node.full)[0]

        for row in current_node.state:
            print(row)

        print(current_node.length)
        print("------------")
        num -= 1
        if num == 0:
            return

        if current_node.state == goal_state:
            return get_result(current_node)
        
        open_set.remove(current_node)
        closed_set.append(current_node)

        for neighbour in get_neighbors(current_node, goal_state):

            for node in closed_set:
                if node.state == neighbour.state:
                    continue

            open_node = None
            for node in open_set:
                if node.state == neighbour.state:
                    open_node = node
                    break


            if open_node == None:
                open_set.append(neighbour)
            else:
                if open_node.length > neighbour.length:
                    open_node.from_node = current_node
                    open_node.length = neighbour.length

    return None















points_list = find_path(

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]],

 [[1, 2, 3],
  [4, 5, 6], 
  [7, 0, 8]]
  
)