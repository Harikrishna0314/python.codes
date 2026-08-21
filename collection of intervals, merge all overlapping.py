a = [[1, 3], [2, 6], [8, 10], [9, 12]]
a.sort()
res = [a[0]]

for b in a[1:]:
    if b[0] <= res[-1][1]:
        res[-1][1] = max(res[-1][1], b[1])
    else:
        res.append(b)

print(res)
