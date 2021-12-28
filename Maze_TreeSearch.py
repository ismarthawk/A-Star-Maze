from pyamaze import maze,agent
import heapq


def heuristic(node) :
    return abs(node[0]-1) + abs(node[1]-1)


def solve(maze : maze) :
    frontier = []
    start = (maze.rows,maze.cols)
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
    
    while frontier :
        fun , node , path  = heapq.heappop(frontier)
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
    
    return None



if __name__ == "__main__" :
    n = int(input("Enter the size of the maze: "))
    m = maze(n, n)
    m.CreateMaze(theme='light')
    a = agent(m, footprints=True)
    result = solve(m)
    print(result)
    if result:
        d = dict()
        for i in range(len(result)):
            if result[i] == (1, 1):
                break
            d[result[i]] = result[i+1]
        print(d.items())
        m.tracePath({
            a: d,
        },delay=20)
    m.run()
