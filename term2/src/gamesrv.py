from tests.resources.data_for_gamesrv.heap_based_priority_queue import *


def dijkstra(server, number_of_vertex, clients, adjacency_list):
    max_ping = 0
    heap = HeapBasedPriorityQueue()
    heap.insert(server, 0)
    dist_to = {}
    for vertex in range(number_of_vertex + 1):
        dist_to[vertex] = float('inf')
    dist_to[server] = 0
    visited = set()

    while heap.array:
        vertex = heap.delete_root()
        if vertex is None:
            break

        if vertex in clients:
            max_ping = max(max_ping, dist_to[vertex])

        visited.add(vertex)
        for neighbour, weight in adjacency_list[vertex - 1]:
            if dist_to.get(neighbour, float('inf')) > dist_to[vertex] + weight:
                dist_to[neighbour] = dist_to[vertex] + weight
                heap.insert(neighbour, dist_to[neighbour])

    return max_ping


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return


def latency(input_file, output_file):
    file = open(input_file, 'r')
    first_line = file.readline()
    if not first_line:
        write_output(output_file, None)
        file.close()
        return

    number_of_vertex, number_of_edges = map(int, first_line.split(' '))
    adjacency_list = [[] for _ in range(number_of_vertex)]
    gamers = list(map(int, file.readline().split(' ')))
    routers = [router for router in range(1, number_of_vertex + 1) if router not in gamers]
    for _ in range(number_of_edges):
        vertex, neighbour, weight = map(int, file.readline().split(' '))
        adjacency_list[vertex - 1].append((neighbour, weight))
        adjacency_list[neighbour - 1].append((vertex, weight))
    file.close()

    minimum_max_ping = float('inf')
    for server in routers:
        minimum_max_ping = min(minimum_max_ping, dijkstra(server, number_of_vertex, gamers, adjacency_list))

    write_output(output_file, minimum_max_ping)
