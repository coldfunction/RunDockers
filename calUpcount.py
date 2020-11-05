import time
import os
import sys
import subprocess

countNum = int(sys.argv[1])
countNum = countNum+1
count = -10

while count!=countNum:
    out_bytes = subprocess.check_output(['docker','ps'])
    out_text = out_bytes.decode('utf-8')
    substring = 'Up'
    count = out_text.count(substring)
    #print(count)
    #time.sleep(1)

