from utilities.graph import Graph
from route_between_nodes_1 import route_between_nodes_1

def main():
    graph = Graph()
    graph.create_graph({'a': ['b', 'f'], 'c': ['b'], 'b': ['d'], 'e': ['a'], 'd': ['a'], 'f': ['e']})

    print "Solution 1: BFS through the graph and find connection"
    print "input: ['a': ['b', 'f'], 'c': ['b'], 'b': ['d'], 'e': ['a'], 'd': ['a'], 'f': ['e']], a: ['b', 'f'], c: ['b'], output: {output}"\
        .format(output=route_between_nodes_1(graph, graph.nodes['a'], graph.nodes['c']))
    print "input: ['a': ['b', 'f'], 'c': ['b'], 'b': ['d'], 'e': ['a'], 'd': ['a'], 'f': ['e']], a: ['b', 'f'], c: ['b'], output: {output}"\
        .format(output=route_between_nodes_1(graph, graph.nodes['c'], graph.nodes['a']))


if __name__ == '__main__':
    main()