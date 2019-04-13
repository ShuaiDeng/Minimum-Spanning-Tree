import sys


class Graph(object):

    def __init__(self, maps):
        self.maps = maps
        self.num = len(maps)

    def get_num(self):
        return self.num

    def get_edges(self):
        edge_list = []
        for i in range(self.num):
            for j in range(self.num):
                if self.maps[i][j] != '0':
                    edge_list.append([i, j, int(self.maps[i][j])])
        edge_list.sort(key=lambda a: a[2])
        # print(edge_list)
        return edge_list


def kruskal(graph):
    ret=[]
    union=[set([i]) for i in range(graph.get_num())]
    for edge in graph.get_edges():
        u,v,_=edge
        if u not in union[v] and v not in union[u]:
            ret.append([u,v])
            union[u].add(v)
            union[v].add(u)
            for i in union[u]:
                union[i]=union[i] | union[u]
            for i in union[v]:
                union[i]=union[i] | union[v] 
    return ret


def read_file(path):
    ret = []
    with open(path, "r") as f:
        for line in f.readlines():
            ret.append(line.split())
    # print(ret)
    return ret
if __name__ == '__main__':
    if(len(sys.argv) < 2):
        sys.exit()
    myGraph = Graph(read_file(sys.argv[1]))
    ans=kruskal(myGraph)
    for line in ans:
        print(line[0],line[1])
