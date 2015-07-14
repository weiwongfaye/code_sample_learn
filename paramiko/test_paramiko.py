__author__ = 'weiwang'
import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('host', username='xxx', password='xxx')
stdin, stdout, stderr = ssh.exec_command("uptime")

print stdout.readlines()[0]
time.sleep(60)
stdin, stdout, stderr = ssh.exec_command("uptime")

print stdout.readlines()[0]


