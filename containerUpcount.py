import time
import os
import subprocess

#docker-compose run --entrypoint '/bin/bash' APP &

i = 0
string1 = "docker-compose run --name test"
string2 = "0"
string3 = " --entrypoint '/bin/bash' APP &"
while i<1:
    print(i)
    string2 = str(i)
    newstring = string1+string2+string3
 #   os.system(newstring)
#    subprocess.run(['docker-compose', 'run', '--entrypoint', '/bin/bash', 'APP'], stdout=subprocess.PIPE)
    subprocess.run(['docker-compose', 'run', '--entrypoint', '/bin/bash', 'APP'], stdout=subprocess.PIPE)

    print(newstring)
    i=i+1
    time.sleep(10)

while True:
    out_bytes = subprocess.check_output(['docker','ps'])
    out_text = out_bytes.decode('utf-8')
    substring = 'Up'
    count = out_text.count(substring)
    print(count)
    time.sleep(1)

