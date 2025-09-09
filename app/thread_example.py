from threading import Thread
import time


def work(n):
    print(f"start {n}")
    time.sleep(0.1)
    print(f"done {n}")

threads = [Thread(target=work, args=(i,)) for i in range(1, 6)]
for t in threads:
    t.start()
for t in threads:
    t.join()


