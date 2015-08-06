import commands
import os

(status_code, result) = commands.getstatusoutput('ls -al '+os.getcwd())

print status_code
print result

# abspath

print os.path.abspath('./test')

