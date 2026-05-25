# class Graphs:
#     def __init__(self,size):
#         self.size=size
#         self.graph=[]
#         self.vertices=[]

#     def add_vertex(self,v):
#         if v in self.vertices:
#             pass
#         else:
#             self.vertices.append(v)
#             temp=[]
#             for i in range(self.size):
#                 temp.append(0)
#             self.graph.append(temp)

#     def add_edges(self,v1,v2,w):
#         i1=self.vertices.index(v1)
#         i2=self.vertices.index(v2)
#         self.graph[i1][i2]=w
    
#     def rem_edges(self,v1,v2):
#         i1=self.vertices.index(v1)
#         i2=self.vertices.index(v2)
#         self.graph[i1][i2]=0

#     def printGr(self):
#         for i in range(0,self.size):
#             for j  in range(0,self.size):
#                 print(self.vertices[i],"->",self.vertices[j],"edge weight:",self.graph[i][j])
#         for i in range(self.size):
#             print(self.graph[i])

# gr=Graphs(4)
# gr.add_vertex(1)
# gr.add_vertex(2)
# gr.add_vertex(3)
# gr.add_vertex(4)

# gr.add_edges(1,2,1)
# gr.add_edges(2,1,1)
# gr.add_edges(1,3,4)
# gr.add_edges(3,4,5)

# gr.printGr()

#adjacency list

# class Graphs:
#     def __init__(self,size):
#         self.size=size
#         self.graph={}

#     def add_vertex(self,v):
#         self.graph[v]=[]

#     def add_edges(self,v1,v2,w):
#         temp=[v2,w]
#         self.graph[v1].append(temp)
    
#     def rem_edges(self, v1, v2):
#         if v1 in self.graph:
#             self.graph[v1] = [pair for pair in self.graph[v1] if pair[0] != v2]

        

#     def printGr(self):
#         for i in self.graph:
#             for j in self.graph[i]:
#                 print(i,"->",j[0],"edge weight:",j[1])

# gr=Graphs(4)

# gr.add_vertex(1)
# gr.add_vertex(2)
# gr.add_vertex(3)
# gr.add_vertex(4)

# gr.add_edges(1,2,3)
# gr.add_edges(2,1,5)
# gr.add_edges(3,4,6)
# gr.add_edges(2,4,8)
# gr.printGr()
# gr.rem_edges(2,4)

# print(gr.graph)
    
#BFS
Graph= {
    1: [2,3],
    2:[4,5],
    3:[6],
    4:[],
    5:[6],
    6:[]
}

# visited=[]
# queue=[]

# def bsf(visited,graph,node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         s=queue.pop(0)
#         print(s, end="")

#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)

# bsf(visited,Graph,2)

#DFS

visited=[]
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,Graph,5)


#if we want all the nodes even if they don't have connections
for node in Graph:
    if node not in visited:
        dfs(visited, Graph, node)

#this is the end of graphs#this is the end of graphs