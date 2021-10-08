import os
import  sys
with open("file","r") as a:
    c=open("file2","w+")
    c.writelines(a.read())
#os.remove("file2")
with open("fil","w+") as d:
    d.writelines(os.listdir())