import time
import sys

text =" Hii I am learning Python "
i = 0

while True:
    sys.stdout.write("\r" + text[i:] + text[:i])
    sys.stdout.flush()
    
   
    i = (i + 1) % len(text)
    
    time.sleep(0.15)  # control speed
