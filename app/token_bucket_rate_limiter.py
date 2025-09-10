import time
from queue import Queue
from threading import Thread

class TokenBucketRateLimiter:
    # rate_per_sec is same as bucket size.
    def __init__(self, rate_per_sec: int):
        self.bucket = Queue(maxsize=rate_per_sec) # Queue is threadsafe.
        self.rate = rate_per_sec
        self.bucket_max_size = rate_per_sec

        # prefill the bucket
        for i in range(self.rate):
            self.bucket.put_nowait(None) # put_nowait is non blocking.

        # Start a deamon thread to refill the bucket.
        refill_thread = Thread(target=self._refill_bucket(), daemon=True)
        refill_thread.start()

    # Refill the bucket.
    def _refill_bucket(self):
        interval = 1 / self.rate
        while True:
            time.sleep(interval)
            if self.bucket.qsize() < self.bucket_max_size:
                self.bucket.put_nowait(None) # put_nowait is non blocking.

    # Acquire token from the bucket.
    def acquire(self):
        self.bucket.get() # # block until a token is available

def worker(id: int, limiter: TokenBucketRateLimiter):
    print(f"thread: {id}. Fetching token.")
    limiter.acquire()
    print(f"thread: {id}. Acquired token.")

if __name__ == "__main__":
    rate_limiter = TokenBucketRateLimiter(100)
    threads = []

    for i in range(10):
        t = Thread(target=worker, args=(i, rate_limiter))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

