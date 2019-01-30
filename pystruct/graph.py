from base import Node

class GraphNode(Node):
    def __init__(self, props=dict()):
        super(self, props)
        self.connections = list()
    
    def add_connection(self, name):
        if name not in self.connections:
            self.connections += [name]
        return self

    def add_connections(self, names):
        for name in names:
            if name not in self.connections:
                self.connections += [name]
        return self

    def remove_connections(self, names):
        for name in names:
            if name in self.connections:
                self.connections.remove(name)
        return self
    
    def remove_connection(self, name):
        if name in self.connections:
            self.connections.remove(name)
        return self
    
    def get_connections(self):
        return self.connections

class Graph:
    def __init__(self, names=list()):
        self.nodes = dict()
        for name in names:
            self.nodes[name] = Node()
    
    def get_node(self, name):
        return self.nodes[name]