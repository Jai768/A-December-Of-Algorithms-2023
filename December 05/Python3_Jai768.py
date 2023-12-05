l=[]
n=int(input())
for i in range(n):
    ele=int(input())
    l+=[ele]
o=0
avg=sum(l)/n
for i in l:
    if i>=avg:
        o+=i
print(o)
