#Simple  Countdown Timer
import time

start = int(input("Enter a start time: "))

while(start != 0):
    print("T-Minus %s seconds" % start)
    start -= 1
    time.sleep(1)

print("Blast Off!")