"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Setup initial state for stack and visited

        def dft_recursion(self, starting_vertex, visited=set(), s=Stack()):
            # Push starting vertix into the end of the stack
            s.push(starting_vertex)
            # Pop the last vertex from the stack
            v = s.pop()
            # If the vertex doesnt already exist in stack then add it to the stack
            if v not in visited:
                visited.add(v)
                print(v)
                # Check the neighbors of the vertex. If it has neighbors use recursion.
                for neighbor in self.vertices[v]:
                    dft_recursion(self, neighbor, visited, s)

        dft_recursion(self, starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # BFS uses Queues (FIFO)
        q = Queue()
        # Enqueue the starting vertex into the queue as a LIST
        q.enqueue([starting_vertex])
        # Create a visited set
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            # Check last element of the path
            check_vertex = path[-1]
            if check_vertex not in visited:
                if check_vertex == destination_vertex:
                    return path
                else:
                    # If it isn't visited, add it to visited set.
                    visited.add(check_vertex)
                    # Check all neighbor vertices and add them to the queue
                    for neighbor in self.vertices[check_vertex]:
                        nextPath = list(path)
                        nextPath.append(neighbor)
                        q.enqueue(nextPath)
        return ('Cannot find path')

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # DFS uses Stacks (LIFO)
        s = Stack()
        # Push the starting vertex into the stack as a LIST
        s.push([starting_vertex])
        # Create a visited set
        visited = set()
        while s.size() > 0:
            path = s.pop()
            # Check the last element of the path
            check_vertex = path[-1]
            if check_vertex not in visited:
                if check_vertex == destination_vertex:
                    return path
                else:
                    # If it isn't the destination vertex, then add to the visited set
                    visited.add(check_vertex)
                    # Check all neighbor vertices and push them to the stack
                    for neighbor in self.vertices[check_vertex]:
                        nextPath = list(path)
                        nextPath.append(neighbor)
                        s.push(nextPath)
        return ('Cannot find path')


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
