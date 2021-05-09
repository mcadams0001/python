from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19]

for num in range(5):
    right_this_minute = datetime.today().second

    if right_this_minute in odds:
        print ("This minute is odd")
    else:
        print ("This minute is even")

    print ("Current time is ", datetime.today().second)
    wait_time = random.randint(1,10)
    time.sleep(wait_time)