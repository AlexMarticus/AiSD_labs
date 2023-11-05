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

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        if vertex == end:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
