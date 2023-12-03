n=int(input("Emter N: "))
l=[]
j=1
for i in range(n):
    ele=int(input("Enter element: "))
    l.append(ele)
max=l[0]
for i in l:
    if i>max:
        j+=1
        max=i
print(j)