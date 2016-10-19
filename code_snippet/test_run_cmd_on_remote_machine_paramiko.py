import sys
import paramiko

try:
    hostname, username, password, targetpath, operation = sys.argv[1:6]
except ValueError:
    print("Failed, call with hostname username password targetpath")

command = "cd {targetpath};{operation}".format(targetpath=targetpath, operation=operation)
print("Command to send: {}".format(command))

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command("cd {targetpath};{operation}".format(targetpath = targetpath,
    operation = operation))
print(stdout.read())
ssh.close()



#$ python test_run_cmd_on_remote_machine_paramiko.py 10.66.128.122 user pass /tmp/ 'ls -alh'
