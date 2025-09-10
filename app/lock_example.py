"""
•	Lock (mutex) → once a thread acquires it, even the same thread can’t acquire it again until it releases. Trying to do so → deadlock.
•	RLock (reentrant lock) → the same thread can re-acquire the lock multiple times. It must release it the same number of times before another thread can acquire it.
"""

from threading import Thread, Lock, RLock
import time, random

counter = 0
lock = Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock: # critical section,
            counter += 1

def simulate_increment():
    threads = [Thread(target=increment, args=(10000,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter: {counter}")

class BankAccount:
    def __init__(self, id: int, balance: float):
        self.id = id
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount: float):
        with self.lock:
            old_balance = self.balance
            time.sleep(random.uniform(0, 0.01))
            self.balance = old_balance + amount

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance:
            return False
        with self.lock:
            old_balance = self.balance
            time.sleep(random.uniform(0, 0.01))
            self.balance = old_balance - amount
            return True

def simulate_deposit_and_withdrawals():
    account = BankAccount(1, 100)
    threads = []
    for _ in range(5):
        threads.append(Thread(target=account.withdraw, args=(30,)))
    for _ in range(5):
        threads.append(Thread(target=account.deposit, args=(20,)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Final balance: {account.balance}")


rlock = RLock()

def reentrant_example(n):
    with rlock:
        print(f"Acquired lock at depth {n}")
        if n > 0:
            reentrant_example(n-1)
        print(f"Releasing lock at depth {n}")

reentrant_example(3)

if __name__ == "__main__":
    simulate_deposit_and_withdrawals()
