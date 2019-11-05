from util import Stack, Queue  # These may come in handy


# Create Graph class and import Stack, Queue classes
# Create vertexes and edges between ancestors
# Use BFS (queues) for traversing the graph
# Create starting max_length and earliest ancestor variables
# Loop through all vertexes and continue to change max_length and earliest ancestor
# Return earliest ancestor
# Remember the same ancestor length edge case

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesnt exist")


def earliest_ancestor(ancestors, starting_node):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # create a graph
    graph = Graph()
    # add all edges from the ancestors
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Link kids to parents, one way up so indexes need to be put in opposite order otherwise change add_edges function in Graph class
        graph.add_edges(pair[1], pair[0])

    # BFS uses Queues (FIFO)
    q = Queue()
    # Enqueue the starting vertex into the queue as a LIST
    q.enqueue([starting_node])

    # Create default max path length and earliest ancestor
    max_path_length = 1
    # Set earliest to -1 to take care of edge case of no parents
    earliest = -1

    while q.size() > 0:
        path = q.dequeue()
        # Check last element of the path
        new_vertex = path[-1]

        # Check if same distance of ancestor, but return the lower index number
        if (len(path) > max_path_length) or (len(path) == max_path_length and new_vertex < earliest):
            earliest = new_vertex
            max_path_length = len(path)

        # Check all neighbor vertices and add them to the queue
        for neighbor in graph.vertices[new_vertex]:
            nextPath = list(path)
            nextPath.append(neighbor)
            q.enqueue(nextPath)
    print(path)
    return earliest
