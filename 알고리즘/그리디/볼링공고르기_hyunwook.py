n, m = map(int, input().split())
k = list(map(int, input().split()))

count = 0

for i in k:
    for j in k:
        if i < j:
            count += 1

print(count)