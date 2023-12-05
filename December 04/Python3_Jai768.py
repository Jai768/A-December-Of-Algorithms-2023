s=input("Enter String: ")
l=[]
for i in range(len(s)):
    for j in range(i+2,len(s)):
        new=s[i:j].lower()
        if new==new[::-1]:
            l+=[s[i:j]]
if l==[]:
    print("Error")
else:
    print(min(l))

