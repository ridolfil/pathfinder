import sys
import numpy as np

def create_rectangular_graph(col, rows):
    
    list = []

    for x in range(col):
        for y in range(rows):
            if y>0: 
                list.append([rows*x+y,rows*x+y-1,1])
            if y<rows-1: 
                list.append([rows*x+y,rows*x+y+1,1])
            if x>0: 
                list.append([rows*x+y,rows*(x-1)+y,1])
            if x<col-1: 
                list.append([rows*x+y,rows*(x+1)+y,1])

    return list

def print_rectangular_graph(col, rows):
    
    try:
        with open("nodes.txt","w") as fl:
            for x in range(col):
                for y in range(rows):
                    if y>0: 
                        fl.write(str( "{0}, {1}, 1\n".format(rows*x+y,rows*x+y-1)))
                    if y<rows-1: 
                        fl.write(str( "{0}, {1}, 1\n".format(rows*x+y,rows*x+y+1)))
                    if x>0: 
                        fl.write(str( "{0}, {1}, 1\n".format(rows*x+y,rows*(x-1)+y)))
                    if x<col-1: 
                        fl.write(str( "{0}, {1}, 1\n".format(rows*x+y,rows*(x+1)+y)))
        fl.closed
    except:
        print "some file error:", sys.exc_info()[0]



#Node class
class Node:

    def __init__(self,_ID):
        self.ID = _ID
        self.neighbours = []
        self.total_dist = sys.float_info.max
        self.isvisited = False

    def getNeighbours(self):
        return self.neighbours
    
    def calculate_distance(other_node):
        raise NotImplementedError
    
    def add_neighbour(self, node, distance):
        self.neighbours.append((node, distance))

    def print_node(self,id):
        print self.ID,"\n"
        print "Distance: ", self.total_dist,"\n"
        print "Neighbours: ", len(self.neighbours),"\n"
        for n in self.neighbours:
           print "-  ID:{0}, Dist:{1}".format(n[0].ID, n[1])


class Pathfinder:

    

    def __init__(self, graph):
        self.start_node = 0
        self.destination = 0
        self.Graph = graph
        self.unvisited_nodes = Graph.nodes_list.keys()

    #def create_list():
    #    return [[x,y] for x in Graph.nodes_list.keys() for y in [sys.float_info.max]*len(Graph.nodes_list.keys())]
            

    def set_initial_node(self, firstNode):
        self.start_node=firstNode.ID
        self.Graph.set_distance(start_node,0)

    def set_final_node(self, final_node):
        self.destination = final_node.ID

    def checkNeighbours(current_node):
        
        neighbours_list = current_node.getNeighbours()

        for n in neighbours_list:
            if n.isvisited==False : #could also be n.ID in unvisited_nodes
                tentative_dist = current.total_length + current_node.calculate_distance(n)
                if  tentative_dist < n.total_length:
                    n.total_length = tentative_dist
        current_node.isvisited = True


    def traverse_graph(self):
        while destination.isvisited==Fase:
            sorted(unvisited_nodes, key= lambda id:self.Graph.get_distance(id), reverse=True)
            current = Graph.get_node(self.unvisited_nodes.pop())
            if current.total_dist < sys.float_info.max:
                checkNeighbours(current)
            else: break


    def get_dist(self):
        return self.destination.total_length



class Graph_Structure:

    def __init__(self,lst):
        self.nodes_list = {}
        create_nodes_list(lst)

    def create_nodes_list(self,lst):
        for edge in lst:
            add_node(edge[0]).add_neighbour(add_node(edge[1]), edge[2])

    def add_node(self,id):
        if id not in nodes_list:
            new_node = Node(id)
            nodes_list.append(new_node)
        return self.nodes_list[id]

    def set_distance(self,id, dist):
       self.nodes_list[id].total_dist = dist

    def get_distance(self, id):
        return self.nodes_list[id].total_dist

    def get_node (self, id): return self.nodes_list[id]


rows = 2
cols = 2

n_list = create_rectangular_graph(rows,cols)

gr = Graph_Structure(n_list)

pf = Pathfinder(gr)
pf.set_initial_node(1)
pf.set_final_node(2)
pf.traverse_graph()
print(pf.get_dist())