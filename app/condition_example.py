"""
Condition:
•	A Condition wraps a Lock.
•	Threads can wait() until notified.
•	Another thread can call notify() (wake one waiter) or notify_all() (wake all waiters).
•	Typical usage pattern:
    with condition:
        while not <predicate>:
            condition.wait()
        # safe to proceed


Difference between `lock` and `condition`
`lock` is used to reserve a resource (a shared data structure) to either update (add, remove items) or read (fetch items).

`condition` is used to reserve the resource and also block the caller thread (consumer in this example) and
unblock other threads (producer in this example) on a certain state of the locked data structure.
I guess the lock is needed just to make sure that no one else is modifying the data structure while its condition (state) is being checked.
"""

# Example 1: Producer–Consumer (classic)
from threading import Thread, Condition
import time

buffer = []
condition = Condition()

def producer():
    for i in range(5):
        time.sleep(1)
        with condition:
            buffer.append(i)
            print(f'Producer: produced {i}')
            condition.notify() # wake one waiting consumer.

def consumer():
    for _ in range(5):
        with condition:
            while not buffer:
                condition.wait()
            item = buffer.pop()
            print(f'Consumer: consumed {item}')

t1 = Thread(target=producer)
t2 = Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()




