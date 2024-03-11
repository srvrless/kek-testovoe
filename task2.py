from collections import Counter


def diversity(A, B):
    set_A = Counter(A)
    set_B = Counter(B)
    diversity_count = 0

    for card, count in set_A.items():
        if card in set_B:
            min_count = min(count, set_B[card])
            diversity_count += count - min_count
    return diversity_count


N, M, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(diversity(A, B), end=" ")

for _ in range(Q):
    type_k, player_k, card_k = input().split()
    type_k = int(type_k)
    card_k = int(card_k)

    if player_k == "A":
        if type_k == 1:
            A.append(card_k)
        else:
            A.remove(card_k)
    else:
        if type_k == 1:
            B.append(card_k)
        else:
            B.remove(card_k)

    print(diversity(A, B), end=" ")
