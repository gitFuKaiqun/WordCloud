__author__ = 'Kaiqun'

import networkx as nx

TheList = [3,5,7,2,6,8,1,9]
G=nx.Graph()

def recur1(InputList):
    global G
    if len(InputList) == 0:
        return InputList
    else:
        tmpMarker = []
        G.add_node(InputList[0])
        tmpMarker.append(0)
        for i in range(len(InputList))[1:]:
            if (InputList[0]-InputList[i])*(InputList[0]-InputList[i]) <= 4:
                G.add_node(InputList[i])
                G.add_edge(InputList[0], InputList[i])
                tmpMarker.append(i)
        discount = 0
        for one in tmpMarker:
            del InputList[one - discount]
            discount += 1
        return recur1(InputList)

def recur2(InputList):
    global G
    if len(InputList) == 0:
        return InputList
    else:
        G.add_node(InputList[0])
        for i in range(len(InputList))[1:]:
            if (InputList[0]-InputList[i])*(InputList[0]-InputList[i]) <= 100:
                G.add_node(InputList[i])
                G.add_edge(InputList[0], InputList[i])
        del InputList[0]
        return recur2(InputList)

recur2(TheList)

print (list(nx.dfs_edges(G,None)))