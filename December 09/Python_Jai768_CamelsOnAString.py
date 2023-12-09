def camel(s):
    n=0
    for i in s:
        if (i.isupper()):
            n+=1
    return n
print(camel(input("Enter String: ")))



