from collections import deque

metro = {
    'Nevskiy': ['Sennaya', 'Vosstaniya'],
    'Sennaya': ['Tehnologicheskiy', 'Pushkinskaya', 'Nevskiy', 'Dostoevskaya'],
    'Tehnologicheskiy': ['Baltiyskaya', 'Phrunzenskaya', 'Sennaya'],
    'Pushkinskaya': ['Obvodniy', 'Dostoevskaya', 'Sennaya'],
    'Vosstaniya': ['Dostoevskaya', 'PloshchadNevskogo', 'Nevskiy'],
    'PloshchadNevskogo': ['Ligovskiy', 'Novocherkasskaya', 'Vosstaniya'],
    'Baltiyskaya': ['Tehnologicheskiy'],
    'Phrunzenskaya': ['Tehnologicheskiy'],
    'Obvodniy': ['Pushkinskaya'],
    'Ligovskiy': ['PloshchadNevskogo'],
    'Novocherkasskaya': ['PloshchadNevskogo'],
    'Dostoevskaya': ['Pushkinskaya', 'Vosstaniya', 'Sennaya']

}


def dfs_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return path

    shortest_path = None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_shortest_path(graph, neighbor, end, path)
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path

    return shortest_path


print(dfs_shortest_path(metro, 'Ligovskiy', 'Pushkinskaya'))
