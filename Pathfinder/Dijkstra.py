import sys
import numpy as np
import matplotlib.pyplot as plt

def create_rectangular_graph(col, rows):
    
    list = []

    for x in range(col):
        for y in range(rows):
            if y>0: 
                list.append([rows*x+y,rows*x+y-1,1])
                if x>0:
                    list.append([rows*x+y,rows*(x-1)+y-1,1.4142])
                if x<col-1:
                    list.append([rows*x+y,rows*(x+1)+y-1,1.4142])
            if y<rows-1: 
                list.append([rows*x+y,rows*x+y+1,1])
                if x>0:
                    list.append([rows*x+y,rows*(x-1)+y+1,1.4142])
                if x<col-1:
                    list.append([rows*x+y,rows*(x+1)+y+1,1.4142])
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
        self.previous = None

    def getNeighbours(self):
        return self.neighbours
    
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
        self.start_node = None
        self.destination = None
        self.Graph = graph
        self.unvisited_nodes = self.Graph.nodes_list.keys()

    #def create_list():
    #    return [[x,y] for x in Graph.nodes_list.keys() for y in [sys.float_info.max]*len(Graph.nodes_list.keys())]
            

    def set_initial_node(self, firstNode):
        self.start_node=self.Graph.get_node(firstNode)
        self.Graph.set_distance(self.start_node.ID,0)

    def set_final_node(self, final_node):
        self.destination = self.Graph.get_node(final_node)

    def checkNeighbours(self, current_node):
        
        neighbours_list = current_node.getNeighbours()

        for n in neighbours_list:
            if n[0].isvisited==False : #could also be n.ID in unvisited_nodes
                tentative_dist = current_node.total_dist + n[1]
                if  tentative_dist < n[0].total_dist:
                    n[0].total_dist = tentative_dist
                    n[0].previous = current_node
        current_node.isvisited = True


    def traverse_graph(self):
        while self.destination.isvisited==False:
            self.unvisited_nodes.sort(key= lambda id:self.Graph.get_distance(id), reverse=True)
            current = self.Graph.get_node(self.unvisited_nodes.pop())
            if current.total_dist < sys.float_info.max:
                self.checkNeighbours(current)
            else: break


    def get_dist(self):
        return self.destination.total_dist

    def return_path(self):
        pth = []
        n= self.destination
        while n != self.start_node: 
            pth.append(n.ID)
            n = n.previous
        pth.append(self.start_node.ID)                    
        return pth[::-1]



class Graph_Structure:

    def __init__(self,lst):
        self.nodes_list = {}
        for edge in lst:
            self.add_node(edge[0]).add_neighbour(self.add_node(edge[1]), edge[2])

    def add_node(self,id):
        if id not in self.nodes_list:
            new_node = Node(id)
            self.nodes_list[id]=new_node
        return self.nodes_list[id]

    def set_distance(self,id, dist):
       self.nodes_list[id].total_dist = dist

    def get_distance(self, id):
        return self.nodes_list[id].total_dist

    def get_node (self, id): return self.nodes_list[id]





rows = 20
cols = 20

n_list = create_rectangular_graph(cols,rows)

gr = Graph_Structure(n_list)

pf = Pathfinder(gr)
pf.set_initial_node(37)
pf.set_final_node(366)
pf.traverse_graph()
print "Total distance: ", pf.get_dist()

route = pf.return_path()


### Draw the path  ###

full_grid = [0] * rows * cols

for i in route:
    full_grid[i]=1

full_grid = np.reshape(full_grid,(cols, rows)).T

ax=plt.gca()
im1 = ax.imshow(full_grid,interpolation='none',origin='upper', cmap=plt.cm.gray)
ax.set_xticks(np.arange(full_grid.shape[1]+1)-0.5,minor=True)
ax.set_yticks(np.arange(full_grid.shape[0]+1)-0.5,minor=True)
ax.grid(which='minor', color='w', linestyle='-',linewidth=1)

plt.show()

