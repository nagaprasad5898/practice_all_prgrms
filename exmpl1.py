import  re
b=input("enter what to search:")
e=b+":.*"
with open("file2","r") as a , open("file","r") as x:
    c=a.read()
    d=re.findall(e, c)
#    print(x.read())


try:
    print(d[0].split(":")[1])
except IndexError:
    print("not in this file")