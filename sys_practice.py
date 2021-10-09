import sys
import platform
print(platform.system())
print(sys.path)
print(sys.platform)
print(sys.executable)
a=sys.modules
c=list(a)
d=input("enter anything :")
"""
with open("moduls.txt","w+") as b:
    for i in c:
        b.writelines("*)")
        b.writelines(i+" ")
"""
print(sys.copyright)
for i in sys.argv:
    print(i)
