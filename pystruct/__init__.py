"""
Pystruct is a library designed to aid math that uses networks or graphs by providing a framework for graphs and other data structures. 
"""

class Node:
    """The basic Node class is use as a parent class for many different structures. """
    def __init__(self, props=dict()):
        """Initializes the Node object. """
        self.properties = props
    
    def add_property(self, prop_name, value=None):
        """Adds a property to the Nodes poperties. """
        if prop_name in self.properties:
            return self
        
        self.properties[prop_name] = value
        return self

    def set_properties(self, prop_name, value):
        """Sets the value of the given value"""
        if prop_name not in self.properties:
            raise KeyError(prop_name)
        
        self.properties[prop_name] = value
        return self
    
    def get_property(self, prop_name):
        """Returns the value assigned to the given property"""
        if prop_name not in self.properties:
            raise KeyError(prop_name)
        
        return self.properties[prop_name]

    