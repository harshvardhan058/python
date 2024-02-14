import time

wait_time = 1
max_retries = 6
attempts = 0

while attempts < max_retries:
    print("Attempt",attempts + 1," - wait time",wait_time,"Seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1