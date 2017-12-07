import networkx as nx
import matplotlib.pylab as plt


def draw_pic(graph):
    global edge_color_map
    edge = []  # store the edge has been add to G
    G = nx.Graph()
    target_edge = []  # store the edge need to be color red

    for node in graph:  # add node
        G.add_node(node)

    for index, node in enumerate(shortest_path_pic):  # pick the edge need to color red into target_edge
        if index < len(shortest_path_pic) - 1:
            target_edge.append([node, shortest_path_pic[index + 1]])

    for outterNode in graph.items():
        for innerNode in outterNode[1].items():
            if [innerNode[0], outterNode[0]] not in edge:  # (a,b)in, then (b,a) should not in
                edge.append([outterNode[0], innerNode[0]])
                G.add_edge(outterNode[0], innerNode[0], weight=innerNode[1])
            if [outterNode[0], innerNode[0]] in edge:
                edge_color_map.append('black')
            elif [outterNode[0], innerNode[0]] in target_edge:
                edge_color_map.pop()
                edge_color_map.append('r')
    nx.draw(G, with_labels=True, edge_color=edge_color_map)
    plt.show()


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    global shortest_path_pic
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')
    # ending condition
    if src == dest:
        # build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
            shortest_path_pic = path
        print('shortest path: ' + str(path) + " cost=" + str(distances[dest]))
    else:
        # if it is the initial run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijkstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


if __name__ == "__main__":
    shortest_path_pic = []  # store shortest path
    edge_color_map = []  # store color
    graph = {'s': {'a': 100, 'b': 1444},
             'a': {'s': 333, 'b': 444, 'c': 118},
             'b': {'s': 422, 'a': 233, 'd': 222},
             'c': {'a': 22, 'd': 722, 't': 444},
             'd': {'b': 11, 'c': 111, 't': 555},
             't': {'c': 313, 'd': 115}}
    dijkstra(graph, 's', 't')
    draw_pic(graph)
