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



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.
    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    Assumes:
        start and end are numbers for existing buildings in graph
    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.
        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    start = Node(start)
    end = Node(end)
    # we can replace dict with tuple to fix performance
    path_best = {'path': None,
                 'total_dist': maxTotalDist,
                 'outdoor_dist': maxDistOutdoors}
    paths = listPaths(digraph, start, end)

    for path in paths:
        total_dist, outdoor_dist = getDistances(digraph, path)
        if total_dist <= maxTotalDist and outdoor_dist <= maxDistOutdoors:
            if total_dist <= path_best['total_dist']:
                path_best.update(path=path,
                                 total_dist=total_dist,
                                 outdoor_dist=outdoor_dist)

    if path_best['path'] is None:
        raise ValueError

    return [node.getName() for node in path_best['path']]  # convert nodes to str
