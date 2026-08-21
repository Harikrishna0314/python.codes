s = "swiss"
result = -1

for c in s:
    if s.count(c) == 1:
        result = c
        break

print(result)
