import time
import subprocess
#out_bytes = subprocess.check_output(['free','-m'])
#out_text = out_bytes.decode('utf-8')
#print(out_text)
#out = out_text.split()
fp = open("memreco.txt", "a")

while True:
    time.sleep(1)
    out_bytes = subprocess.check_output(['free','-m'])
    out_text = out_bytes.decode('utf-8')
    out = out_text.split()
    fp.write("test!")
#    print(out[8])

fp.close();
