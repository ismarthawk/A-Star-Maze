# Tree Search Algorithm.
# pyamaze is a module that is used to create a maze and to operate an agent on the maze.
from pyamaze import maze,agent
# heapq is a module which is used to implement a priority queue.
import heapq

# To calculate the heuristic value of the node.h(n)
# Taking the Manhattan distance to be the heuristic value.
def heuristic(node) :
    return abs(node[0]-1) + abs(node[1]-1)


# This is the main function which is used to implement the A* algorithm.
def solve(maze : maze) :
    # Frontier is the priority queue.
    frontier = []
    start = (maze.rows,maze.cols)
    # The start nodes' adjacent/child nodes are added to the frontier.
    # We maintain the path,current node.
    for direction in "NEWS" :
        if maze.maze_map[start][direction] :
            if direction == 'E' :
                child = (start[0],start[1]+1)
            if direction == 'W' :
                child = (start[0],start[1]-1)
            if direction == 'N' :
                child = (start[0]-1,start[1])
            if direction == 'S' :
                child = (start[0]+1,start[1])
            heapq.heappush(frontier,(heuristic(child)+1,child,[start,child]))
    
    # While the frontier is not empty the following steps are performed.

    while frontier :
        fun , node , path  = heapq.heappop(frontier)
        # If the node is the goal node then the path is returned.
        if node == (1,1) :
            return path
        for direction in "NEWS" :
            if maze.maze_map[node][direction] :
                if direction == 'E' :
                    child = (node[0],node[1]+1)
                if direction == 'W' :
                    child = (node[0],node[1]-1)
                if direction == 'N' :
                    child = (node[0]-1,node[1])
                if direction == 'S' :
                    child = (node[0]+1,node[1])
                heapq.heappush(frontier,(heuristic(child)+len(path)+1,child,path+[child]))
    # if the path is not found then the path is returned as None.
    return None



if __name__ == "__main__" :
    # Takes the size of the maze as input.
    n = int(input("Enter the size of the maze: "))
    # creating a maze of size n*n.
    m = maze(n, n)
    m.CreateMaze(theme='light')
    a = agent(m, footprints=True)
    result = solve(m)
    # This solves the maze and displays the path.
    print(result)
    if result:
        d = dict()
        for i in range(len(result)):
            if result[i] == (1, 1):
                break
            d[result[i]] = result[i+1]
        print(d.items())
        # This simulates the agent on the path.
        m.tracePath({
            a: d,
        },delay=20)
    else :
        print("No path found")
    m.run()
