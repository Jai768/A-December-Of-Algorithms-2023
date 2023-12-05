n = int(input())
l = []
for i in range(n):
    ele = int(input())
    l += [ele]
print(sum(l))
print(l.index(max(l)))

