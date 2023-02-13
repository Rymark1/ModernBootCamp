# A graph is a grouping of vertices in which a vertex points to other vertex in some pattern.  An example of this could
# be taking 2 different ways home from work.  I could travel A -> B -> C for my roads, but if there is an accident
# between A -> B, it may be be quicker to go A -> D -> E -> C.  This is because each path can be weighted differently.
#
#      Regular optimized route (A, B, C)
#             5             This is optimal because the sum of the weighted path for A-B-C is 4 + 4 = 8.
#        D ------- E
#    4  /           \   4
#      /             \
#     A ----- B ----- C
#         4       4
#
#      NonRegular optimized route (A, D, E, C)
#             5             This is optimal because the sum of the weighted path for A-B-C is 10 + 6 = 16 vs
#        D ------- E                                                         A-D-E-C which is 4 + 5 + 4 = 13
#    4  /           \   4
#      /             \
#     A ----- B ----- C
#         10      6
#
#  In addition each vertex when pointing can be directional (point in one direction like a one way road) or
#  bidirectional which is called an edge.  As shown above they can be weighted.  Another way we can view this is when
#  we looked at a linked list, it was a straight connection of nodes linked 1 way.
#  We determined that a tree that connection only on one side via larger values was also a linked
#  list since it was a straight path.  A graph is a form of a tree since it can branch out in multiple directions and
#  each vertex can connect to as many other vertices as it needs.  In this way, a graph can also be a lined list.
#
# Adjacency Matrix                          Listing out a matrix of all node connections
#                 A                                | A | B | C | D | E |
#               /    \                           A | 0 | 1 | 0 | 0 | 1 |   1 = connection between vertices
#              E      B                          B | 1 | 0 | 1 | 0 | 0 |   2 = no connection between vertices
#              \      /                          C | 0 | 1 | 0 | 1 | 0 |   If it is weighted, we store the weight
#               D----C                           D | 0 | 0 | 1 | 0 | 1 |   instead of 1 or 0
#                                                E | 1 | 0 | 0 | 1 | 0 |
#
#  Adjacency List
# We create a dictionary of keys which are each vertex, and values which are a list of available vertices
#                  A                                {
#                /    \                              'A': ['B', 'E'],
#               E      B                             'B': ['A', 'C'],
#               \      /                             'C': ['B', 'D'],
#                D----C                              'D': ['C', 'E'],
#                                                    'E': ['A', 'D']
#                                                   }
#
#  Big O for this is different for an adjacency list and an adjacency table.  An AL only store the vertex and the edges
#  it's connected too while an AM has to store all the one's it isn't connected too.
#
#  This makes Big O:    AM = O(|V|^2) sum of all vertices raised to the second power
#                       AL = O(|V|+|E|) the sum of all vertices and the sum of all edges
#  Adding a vertex:     AM = O(V^2)
#                       AL = O(1)
#  Adding an edge:      AM = O(1)
#                       AL = O(1)
#  Removing an edge:    AM = O(1)
#                       AL = O(|E|)
#  Removing a Vertex:   AM = O(|V|^2)
#                       AL = O(|V|+|E|)
#

class Graph:
    def __init__(self):
        self.adj_list = {}

    def clear_all(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1 ,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for vert in self.adj_list.values():
                try:
                    vert.remove(vertex)
                except ValueError:
                    pass
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()
print("\nTesting adding edge")
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_edge(1,2)
my_graph.print_graph()
print("\nTesting removing edge")
my_graph.clear_all()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")
my_graph.print_graph()
my_graph.remove_edge("A", "B")
my_graph.remove_edge("A", "D")
my_graph.print_graph()
print("\nTesting removing vertex")
my_graph.clear_all()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")
my_graph.print_graph()
my_graph.remove_vertex("D")
my_graph.print_graph()
