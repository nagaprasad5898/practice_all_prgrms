import logging
import paramiko
logging.basicConfig(filename="paramiko1.log",level=logging.INFO,format="%(lineno)d:%(asctime)s:%(filename)s:%(message)s:")
obj = paramiko.SSHClient()
obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
obj.connect(hostname="18.217.196.188",username="ubuntu",password="Grandpa@143")
#logging.info("log into server as lucky")
l=["hostname","ls -l","ifconfig","dmidcore"]
for i in l:
    stdin ,stdout,stderr=obj.exec_command(i)
    print(stdout.read().decode())
    logging.error(stderr.read().decode())


