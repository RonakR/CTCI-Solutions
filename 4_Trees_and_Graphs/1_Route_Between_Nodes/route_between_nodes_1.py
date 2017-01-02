from utilities.queue import Queue

def route_between_nodes_1(graph, node_start, node_end):
    q = Queue()
    root = node_start
    does_path_exist = False

    for n, c in graph.nodes.iteritems():
        c.visited = False

    q.add(root)
    root.visited = True

    while not q.isEmpty():
        for child in q.remove().children:
            if not graph.nodes[child].visited:
                if graph.nodes[child].data == node_end.data:
                    does_path_exist = True
                    break
                graph.nodes[child].visited = True
                q.add(graph.nodes[child])

    return does_path_exist