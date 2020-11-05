import subprocess
import threading
import time
import sys

Go_threads = True
memCount = 0

class AsyncWrite(threading.Thread):
   def __init__(self, text, out):
      threading.Thread.__init__(self)
      self.text = text
      self.out = out
   def run(self):
      f = open(self.out, "a")
      #f.write(self.text + '\n')
      pivo = int(self.text) 
      while Go_threads != False:
         time.sleep(1); 
         out_bytes = subprocess.check_output(['free','-m'])
         out_text = out_bytes.decode('utf-8')
         out = out_text.split()
         diff = int(out[8]) - pivo
         #f.write(out[8] + '\n')
         f.write(str(diff) + '\n')
         global memCount
         memCount = memCount+1
         #global stop_threads
         #if stop_threads:
            #break
      
      f.close()
  #    time.sleep(3)
  #    print ("Finished Background file write to " + self.out)
def Main():

   out_bytes = subprocess.check_output(['free','-m'])
   out_text = out_bytes.decode('utf-8')
   out = out_text.split()
#    print(out[8])
   message = out[8] 
   background = AsyncWrite(message,'memrecord.txt')
   #print threading.enumerate()
#   stop_threads = False;   
   background.start()

   print("okok do some okok")
   #time.sleep(10) 


   start = time.time()

   #docker-compose run -d --entrypoint 'bash work.sh' APP
   totalNum = sys.argv[1]
   for i in range(int(totalNum)):
      cname = "--name=test"
   #myid = sys.argv[1]
      myid = str(i)
      cname = cname + myid
      subprocess.run(['docker-compose', 'run', '-d', cname, '--entrypoint', 'bash work.sh', 'APP'], stdout=subprocess.PIPE)

   #time.sleep(50)


   countNum = int(totalNum)
   count = -10
   while count!=countNum:
      out_bytes = subprocess.check_output(['docker','ps'])
      out_text = out_bytes.decode('utf-8')
      substring = 'Up'
      count = out_text.count(substring)

   end = time.time()
   print(end-start)


   #global Go_threads  
   #Go_threads = False  
   #print("okok stop thread")
   global memCount
   print(memCount)
   background.join()
   print ("Waited until thread was complete")
   # print (threading.enumerate())
if __name__ == '__main__':
   Main()

#python3 meminfo.py > memreco.txt &
#docker-compose run --entrypoint 'bash work.sh' APP &


