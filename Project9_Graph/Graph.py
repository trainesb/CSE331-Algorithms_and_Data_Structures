########################################
# PROJECT: Graph
# Author: Ben Traines
########################################

import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Adds a vertex id to the path
            :param vertex: vertex to add
            :return: None
            """
            if vertex not in self.vertices:
                self.vertices.append(Graph.Vertex(vertex).ID)
            return None

        def remove_vertex(self):
            """
            Removes the vertex which was last added to the path
            :return: None
            """
            if self.is_empty() is False:
                self.vertices.pop()
            return None

        def last_vertex(self):
            """
            Returns the id of the vertex that was last added to the path
            :return: id of the vertex that was last added, if the path is empty then return None
            """
            if not self.is_empty():
                return self.vertices[-1]
            return None

        def is_empty(self):
            """
            Checks if the path is empty
            :return: True if empty, else False
            """
            if not self.vertices:
                return True
            return False

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Adds an edge to the vertex given destination
            :param destination: The destination vertex
            :return: None
            """
            if self.get_edge(destination) is None:
                self.edges.append(Graph.Edge(self, destination))
            return None

        def degree(self):
            """
            Return the # of outgoing edges (degree) of the vertex
            :return: # of outgoing edges of the vertex
            """
            degree = 0
            for edge in self.edges:
                degree += 1
            return degree

        def get_edge(self, destination):
            """
            Returns the edge that goes to destination
            :param destination: The destination vertex
            :return: Edge of a specified destination node if found, else None
            """
            for i in self.edges:
                if i.destination == destination:
                    return i
            return None

        def get_edges(self):
            """
            Returns a list of all of the edges
            :return: list of all of the edges
            """
            return self.edges

        def set_fake(self):
            """
            Set the vertex as a fake
            :return: no return
            """
            self.fake = True

        def visit(self):
            """
            Sets the vertex as visited
            :return: no return
            """
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        Returns the vertex with ID
        :param ID: The ID of the vertex to find
        :return: vertex if found, else None
        """
        if ID in self.adj_list:
            return self.adj_list[ID]
        else:
            return None

    def construct_graph(self):
        """
        If a filename is given, read file to create the graph and disregard the size and connectedness. If no file is
        given use generate_edges() to create the graph.

        'GraphError' is raised when an
        - Incorrect filename is given
        - There is no filename and it's size isn't greater than 0
        - connectedness can't be in the range [0,1].
        :return: [source, destination]
        """
        if self.filename is not None:
            try:
                file = open(self.filename, 'r')
            except FileNotFoundError:
                raise GraphError

            for line in file:
                ID, dest = line.strip().split()
                ID = int(ID)
                dest = int(dest)
                vertex = self.get_vertex(ID)
                dest_vertex = self.get_vertex(dest)

                if vertex is None:
                    vertex = self.Vertex(ID)
                    self.size += 1
                vertex.add_edge(dest)
                self.adj_list[vertex.ID] = vertex

                if dest_vertex is None:
                    dest_vertex = self.Vertex(dest)
                    self.size += 1
                    self.adj_list[dest_vertex.ID] = dest_vertex

        else:
            # Size has to be larger than 0
            if self.size <= 0:
                raise GraphError

            # Connectedness has to be between [0,1] and can't be 0
            if self.connectedness > 1 or self.connectedness <= 0:
                raise GraphError

            for i in range(self.size):
                vertex = self.Vertex(i)
                self.adj_list[vertex.ID] = vertex
            for id, dest_id in self.generate_edges():
                vertex = self.get_vertex(id)
                vertex_des = dest_id
                vertex.add_edge(vertex_des)

    def BFS(self, start, target):
        """
        Finds a path to the target from start using Breadth First Search
        :param start: ID of the starting vertex
        :param target: ID of the terminating vertex
        :return: If target isn't found than return an empty path, else return the path from start to target.
        """
        path = Graph.Path()
        path.add_vertex(self.get_vertex(start).ID)
        while path.is_empty() is False:
            next_ver = []
            for id in path.vertices:
                vertex = self.get_vertex(id)
                edges = vertex.get_edges()
                for edge in edges:
                    dest = edge.destination
                    dest_vertex = self.get_vertex(dest)
                    if dest_vertex.visited is False:
                        dest_vertex.visited = True
                        next_ver.append(dest)
            if not next_ver:
                return path
            next_id = next_ver.pop()
            path.add_vertex(self.get_vertex(next_id).ID)
            if path.last_vertex() == target:
                return path

    def DFS(self, start, target, path=Path()):
        """
        Depth First Search, is a recursive search to find a path to the target vertex from start
        :param start: ID of the starting vertex
        :param target: ID of the terminating vertex
        :param path:
        :return:
        """
        vertex = self.get_vertex(start)
        vertex.visited = True
        path.add_vertex(vertex.ID)

        for edge in vertex.get_edges():
            dest = edge.destination
            self.DFS(dest, target, path)

            if path.last_vertex() == target:
                return path

            path.remove_vertex()

def fake_emails(graph, mark_fake=False):
    """
    Finds all of the fake vertices, sets them to be fake, and adds their ID's to a list
    :param graph: Graph to check in for fake vertices
    :param mark_fake: If 'True', than set the fake flag on all fake vertices
    :return: A list of fake vertex ID's
    """

    def check_fake_emails(start, emails=list()):
        """
        Starting at start, finds all fake emails that can be reached from start and removes the edge connected the fake
        address
        :param start: ID of the vertex to start at
        :param emails: A list of all fake emails found
        :return:
        """
        v = graph.get_vertex(start)
        if v.visited is False:
            v.visited = True
            degree = v.degree()
            if degree == 0:
                if mark_fake is True:
                    v.fake = True
                emails.append(v.ID)

            else:
                edges = v.get_edges()
                for edge in edges:
                    dest_ver = graph.get_vertex(edge.destination)
                    if dest_ver.visited is False:
                        check_fake_emails(dest_ver.ID, emails)

    fake_list = list()
    for edge in graph.adj_list:
        vertex = graph.get_vertex(edge)
        if vertex.visited is False:
            check_fake_emails(vertex.ID, fake_list)

    for ver in graph.adj_list:
        rmv = list()
        ver = graph.get_vertex(ver)
        if ver.fake is False:
            edges = ver.get_edges()

            for edg in edges:
                if edg.destination in fake_list:
                    rmv.append(edg)
            for i in rmv:
                ver.edges.remove(i)
                if len(ver.get_edges()) == 0:
                    ver.fake = True
                    fake_list.append(ver.ID)
    return fake_list
