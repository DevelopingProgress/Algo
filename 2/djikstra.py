class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        return self.key

    def add_neighbour(self, dest, weight):
        self.points_to[dest] = weight

    def get_neighbours(self):
        return self.points_to.keys()

    def get_weight(self, dest):
        return self.points_to[dest]

    def set_weight(self, dest, weight):
        self.points_to[dest] = weight

    def does_it_point_to(self, dest):
        return dest in self.points_to


def johnson(g):
    g.add_vertex('q')

    for v in g:
        g.add_edge('q', v.get_key(), 0)

    bell_dist = bellman_ford(g, g.get_vertex('q'))

    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[v] - bell_dist[n])

    del g.vertices['q']

    distance = {}

    for v in g:
        distance[v] = dijkstra(g, v)

    for v in g:
        for w in g:
            distance[v][w] += bell_dist[w] - bell_dist[v]

    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[n] - bell_dist[v])

    return distance


def bellman_ford(g, source):
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0

    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))

    return distance


def dijkstra(g, source):
    unvisited = set(g)
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0

    while unvisited != set():

        closest = min(unvisited, key=lambda v: distance[v])

        unvisited.remove(closest)

        for neighbour in closest.get_neighbours():
            if neighbour in unvisited:
                new_distance = distance[closest] + closest.get_weight(neighbour)
                if distance[neighbour] > new_distance:
                    distance[neighbour] = new_distance

    return distance


g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('johnson')
print('display')
print('quit')

while True:
    do = input('What would you like to do? ').split()
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                else:
                    print('Edge already exists.')

    elif operation == 'johnson':
        distance = johnson(g)
        print('Shortest distances:')
        for start in g:
            for end in g:
                print('{} to {}'.format(start.get_key(), end.get_key()), end=' ')
                print('distance {}'.format(distance[start][end]))

    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()

        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()

    elif operation == 'quit':
        break
