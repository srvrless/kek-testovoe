def compute_language_barrier(N, languages, hierarchy):
    graph = {}
    for i in range(0, 2 * (N + 1), 2):
        manager = hierarchy[i]
        subordinate = hierarchy[i + 1]
        if manager not in graph:
            graph[manager] = []
        graph[manager].append(subordinate)

    def find_language_barrier(employee, language):
        queue = [(employee, 0)]
        visited = set()
        while queue:
            current_employee, barrier = queue.pop(0)
            if languages[current_employee] == language:
                return barrier
            visited.add(current_employee)
            if current_employee in graph:
                for subordinate in graph[current_employee]:
                    if subordinate not in visited:
                        queue.append((subordinate, barrier + 1))
        return -1


    barriers = []
    for i in range(1, N + 1):
        language = languages[i - 1]
        barrier = find_language_barrier(i, language)
        barriers.append(barrier)

    return barriers


N = int(input())
languages = input().split()
hierarchy = list(map(int, input().split()))

barriers = compute_language_barrier(N, languages, hierarchy)
print(*barriers)
