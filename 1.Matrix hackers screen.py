import random
import time
chars = "01"
while True:
    line="".join(random.choice (chars) for i in range(300))
    print(line)
    time.sleep(0.05)

