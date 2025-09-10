from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time

"""
Diff between spawning threads and using `ThreadPoolExecutor`:

When you spawn thread, you have to create as many threads as the number of times you want to run the function because 
you have to assign each run to a separate thread.
In case of `ThreadPoolExecutor`, you can configure the executor with `max_workers` and then assign as many function 
calls you want. The executor will distribute the calls amongst the workers.
"""

def work(n):
    print(f"This is {n}")
    time.sleep(0.1)
    return n * n


def use_threads():
    threads = [Thread(target=work, args=(i,)) for i in range(1, 20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

"""
What a Future is
	•	In Python’s concurrent.futures module, a Future is a class (concurrent.futures.Future).
	•	It’s an object that represents a computation that may not have finished yet.
	executor.submit() method returns a Future instance.
	•	It has methods like:
	•	.result() → block until the computation is done, then return the value (or raise the exception).
	•	.done() → check if it’s finished.
	•	.exception() → see if the function raised an error.
"""
def use_threadpool():
    print("Calling ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(work, i) for i in range(1, 20)]
        results = [f.result() for f in futures]
    print(results)

if __name__ == "__main__":
    use_threadpool()


