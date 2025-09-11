import time
import sys

text = " Hello, this is flowing text!   "
i = 0

while True:
    # Print the rotated string
    sys.stdout.write("\r" + text[i:] + text[:i])
    sys.stdout.flush()
    
    # Move the index
    i = (i + 1) % len(text)
    
    time.sleep(0.15)  # control speed
