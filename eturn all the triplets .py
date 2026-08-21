a = [-1, 0, 1, 2, -1, -4]
a.sort()
res = set()

for i in range(len(a)):
    seen = set()
    for j in range(i + 1, len(a)):
        need = -a[i] - a[j]
        if need in seen:
            res.add((a[i], need, a[j]))
        seen.add(a[j])
print([list(x) for x in res])
