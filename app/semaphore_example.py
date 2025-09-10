from threading import Thread, Semaphore
import time

sem = Semaphore(3) # allow only 3 concurrent threads.

def print_job(user_id):
    with sem: # acquire on enter, release on exit.
        print(f"User: {user_id} is printing ...")
        time.sleep(2)
        print(f"User: {user_id} finished printing.")

threads = [Thread(target=print_job, args=(i, )) for i in range(1, 21)]
for t in threads:
    t.start()
    print(f'Started thread: {t.name}')

for t in threads: t.join()