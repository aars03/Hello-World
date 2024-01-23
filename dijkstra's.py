
# takes the graph and the starting node
# returns a list of distances from the starting node to every other node
from numpy import Inf
def dijkstra(graph, start):
    l = len(graph)
    
    # initialize all node distances as infinite
    dist = [Inf for _ in range(l)]
    
    # set the distance of starting node as 0
    dist[start] = 0
    
    # create a list that indicates if a node is visited or not
    vis = [False for _ in range(l)]
    
    # iterate over all the nodes
    for _ in range(l):
        
        # set u=-1 to indicate a current starting node
        u = -1
        
        # iterate over all the nodes to check the status of the visit 
        for x in range(l):
            # now if the 'x' node is not visited yet or the distance we have currently for it is less than the distance to the start node then update the current node as the 'x'
            if not vis[x] and (u == -1 or dist[x] < dist[u]):
                u = x
                
        # check if we have visited all the nodes or we haven't reached the node
        if dist[u] == Inf:
            break
            
        # set the currently running node as visited
        vis[u] = True
        
       # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance.
        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                
    # now at last return the list which contains the shortest path to each node from that given node            
    return dist

graph = {
    0: [(1, 5),(6,11)],
    1: [(0, 5), (2, 7),(5,5),(6,3),(7,6)],
    2: [(1, 7), (3, 8),(5,1)],
    3: [(2, -8), (5, 9),(4,10)],
    4: [(5, 1), (3, 10),],
    5: [(3,9),(4,1),(6,2),(2,-1),(1,5)],
    6: [(5,2),(1,3),(0,11),(7,9)],
    7: [(1,6),(6,9)]
}
print(dijkstra(graph,0))


