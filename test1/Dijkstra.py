import sys

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

print create_rectangular_graph(2,2)


#Node class
class Node:

    def _init_(self,_ID):
        self.ID = _ID
        self.neighbours = []
        self.total_length = 0
        self.isvisited = False

    def getNeighbours():
        raise NotImplementedError
    
    def calculate_distance(other_node):
        raise NotImplementedError
    
    def add_neighbour(node, distance):
        neighbours.append((node, distance))

    def print_node(id):
        print ID,"\n"
        print "Neighbours: ", len(neighbours),"\n"
        for n in neighbours:
           print "-  ID:{0}, Dist:{1}".format(n[0].ID, n[1])


class Pathfinder:

    

    def _init_(self, edges_list):
        self.start_node
        self.nodes_list = create_list(edges_list)

    def set_initial_node(firstNode):
        start_node=firstNode

    def checkNeighbours(current_node):
        
        neighbours_list = current_node.getNeighbours()

        for n in neighbours_list:
            if n.isvisited==False :
                tentative_dist = current.total_length + current_node.calculate_distance(n)
                if  tentative_dist < n.total_length:
                    n.total_length = tmp_dist
        
        current_node.isvisited = True


    def traverse_graph():
       
        len = len(nodes_list)
        for i in range(len):
            nodes_list.sort(key= lambda n:n.total_length, reverse=True)

            current = nodes_list.pop()

            checkNeighbours(current)






class Graph_Structure:

    def _init_(self):
        nodes_list = {}

    def create_nodes_list(lst):
        for edge in lst:
            add_node(edge[0]).add_neighbour(add_node(edge[1]), edge[2])

    def add_node(id):
        if id not in nodes_list:
            new_node = Node(id)
            nodes_list.append(new_node)
        return nodes_list[id]

    