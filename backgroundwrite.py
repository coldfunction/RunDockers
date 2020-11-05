import threading
import time
class AsyncWrite(threading.Thread):
   def __init__(self, text, out):
      threading.Thread.__init__(self)
      self.text = text
      self.out = out
   def run(self):
      f = open(self.out, "a")
      f.write(self.text + '\n')
      f.close()
      time.sleep(3)
      print ("Finished Background file write to " + self.out)
def Main():
   message = input("Enter a string to store:" )
   background = AsyncWrite(message,'out.txt')
   #print threading.enumerate()
   background.start()
   print ("The program can continue while it writes in another thread")
   num = int(input("Entered number is : "))
   if (num%2==0):
      print("Entered number is Even")
   else:
      print("Entered number is ODD")
   background.join()
   print ("Waited until thread was complete")
   # print (threading.enumerate())
if __name__ == '__main__':
   Main()
