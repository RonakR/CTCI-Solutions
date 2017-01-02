from utilities.graph_node import GraphNode

class Graph:

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        retStr = ""
        for n,c in self.nodes.iteritems():
            retStr += str(c) + ", "

        return retStr

    def create_graph(self, nodes):
        for node, children in nodes.iteritems():
            self.nodes[node] = GraphNode(node, children)


# graphDic={}
# graphDic["a"] = ["b","f"]
# graphDic["b"] = ["d"]
# graphDic["c"] = ["b"]
# graphDic["d"] = ["a"]
# graphDic["e"] = ["a"]
# graphDic["f"] = ["e"]
# print graphDic

graph = Graph()
graph.create_graph({'a': ['b', 'f'], 'c': ['b'], 'b': ['d'], 'e': ['a'], 'd': ['a'], 'f': ['e']})
print graph