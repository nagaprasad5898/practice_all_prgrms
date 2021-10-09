import os
import platform
import paramiko



#from getpass import getpass

ip = "18.217.196.188"
username="ubuntu"
passwrd = "Grandpa@143"
print("pleas wait for some time....")
obj=paramiko.SSHClient()
obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#obj.load_system_host_keys()
print("connecting to server.....")
obj.connect(hostname=ip,username=username,password=passwrd)
cmd=input("enter the command :")
stdin ,stdout,stderr = obj.exec_command(cmd)
print(stdout.read().decode())
print(stderr.read().decode())
