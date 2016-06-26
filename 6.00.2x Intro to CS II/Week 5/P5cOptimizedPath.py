def getDistances(digraph, path):
    """Returns total & outdoor distances for given path."""
    total_dist = 0
    outdoor_dist = 0
    for i in range(len(path) - 1):
        for node, edge in digraph.edges[path[i]]:
            if node == path[i + 1]:
                total_dist += edge.getTotalDistance()
                outdoor_dist += edge.getOutdoorDistance()
    return (total_dist, outdoor_dist)


def listPaths(digraph, start, end, path=[]):
    """Returns all paths from start to end."""
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in digraph.childrenOf(start):
        if node not in path:
            new_paths = listPaths(digraph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


def DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[], path_best=None):
   
    path = path + [start]
    if start == end:
        return path

    for node in digraph.childrenOf(start):
        if node not in path:
            new_path = DFS(digraph, node, end, maxTotalDist, maxDistOutdoors, path, path_best)
            if new_path is not None:
                total_dist, outdoor_dist = getDistances(digraph, new_path)
                if total_dist <= maxTotalDist and outdoor_dist <= maxDistOutdoors:
                    path_best = new_path
                    maxTotalDist = total_dist

    return path_best


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    start = Node(start)
    end = Node(end)

    path_best = DFS(digraph, start, end, maxTotalDist, maxDistOutdoors)

    if path_best is None:
        raise ValueError

    return [node.getName() for node in path_best]  # convert nodes to str


class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest, edge.getTotalDistance(), edge.getOutdoorDistance()))
   
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res += '{0}->{1} ({2}, {3})\n'.format(k, d[0], float(d[1]), float(d[2]))
        return res
       
    def childrenOf(self, node):
        res = []
        for e in self.edges[node]:
            res.append(e[0])
        return res        
   
class WeightedEdge(Edge):
    def __init__(self, src, dest, dist, out_dist):
        self.src = src
        self.dest = dest
        self.dist = dist
        self.out_dist = out_dist
       
    def getTotalDistance(self):
        return self.dist
       
    def getOutdoorDistance(self):
        return self.out_dist
       
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.dist, self.out_dist)
        
