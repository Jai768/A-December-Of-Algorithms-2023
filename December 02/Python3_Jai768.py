l=[]
ul=[]
c=[]
n=int(input())
for i in range(n):
    ele=int(input())
    l+=[ele]
for i in l:
    if i not in ul:
        ul.append(i)
for i in ul:
    c+=[l.count(i)]
print(c)
