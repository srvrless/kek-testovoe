n = int(input())

arrays = []
for _ in range(n):
    size = int(input())
    array = list(map(int, input().split()))
    arrays.append(array)

prefix_sums = []


for array in arrays:
    prefix_sum = [0] * (len(array) + 1)
    for i in range(len(array)):
        prefix_sum[i + 1] = prefix_sum[i] + array[i]
    prefix_sums.append(prefix_sum)

total_similarity = 0

for i in range(n):
    for j in range(i + 1, n):
        similarity = 0

        for k in range(1, min(len(arrays[i]), len(arrays[j])) + 1):
            if prefix_sums[i][k] == prefix_sums[j][k]:
                similarity += 1
            else:
                break
        total_similarity += similarity

print(total_similarity)
