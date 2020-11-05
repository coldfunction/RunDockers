import time
import os
import sys
import subprocess

cname = "--name=test"
myid = sys.argv[1]
cname = cname + myid
subprocess.run(['docker-compose', 'run', cname, '--entrypoint', '/bin/bash', 'APP'], stdout=subprocess.PIPE)


