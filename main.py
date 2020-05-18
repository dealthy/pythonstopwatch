import time
import sys

now = time.time()
future = now + int(sys.argv[1]) * 60
while time.time() < future:
    pass
print("time is up")