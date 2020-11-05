import time
import os
import sys
import subprocess

out_bytes = subprocess.check_output(['docker','ps'])
out_text = out_bytes.decode('utf-8')
substring = 'Up'
count = out_text.count(substring)
print(count)

