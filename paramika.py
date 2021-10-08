import os
import platform

print(dir(os))
''' 

from getpass import getpass
host = "s7works"
username=(input("enter username :") or "kanna")
passwrd = getpass("enter password :")
print(username)
'''
details=platform.uname()
print(details)