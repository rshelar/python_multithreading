"""
SystemClock
	•	sleep(secs) calls time.sleep(secs), which blocks the calling thread for at least secs of real (wall) time.
	•	There’s no programmatic “unblock early” knob you control. (Technically, a signal can interrupt sleep and raise, but that’s not a coordination mechanism you rely on in normal app code.)
	•	Use time.monotonic() for elapsed-time math; it returns a float seconds counter that only increases.

ManualClock
	•	Doesn’t use real time; it models simulated time with a counter (_t).
	•	sleep(secs): computes target = _t + secs, then waits on a Condition until _t reaches target. The thread is blocked on the condition (not “sleeping” by timer).
	•	advance(secs): increments _t and calls notify_all() so waiters wake, re-acquire the lock, re-check (_t >= target), and proceed if satisfied.
	•	(If you use a small timeout in wait(), that’s just to periodically re-check or respond to stop flags; with pure wait(), they’ll block until notified.)

notify_all only notifies the blocked threads to check the condition. It does not unblock them.
"""

import time, threading

class Clock:
    def monotonic(self) -> float:
        pass

    def sleep(self, secs: float) -> None:
        pass

class SystemClock(Clock):
    def monotonic(self) -> float:
        return time.monotonic()

    def sleep(self, secs: float) -> None:
        time.sleep(secs)

"""
Another observation - Difference between `lock` and `condition`
`lock` is used to reserve a resource (a shared data structure) to either update (add, remove items) or read (fetch items).
`condition` is used to reserve the resource and also block the caller thread (consumer in this example) and 
unblock other threads (producer in this example) on a certain state of the locked data structure. 
I guess the lock is needed just to make sure that no one else is modifying the data structure while its condition (state) is being checked.
do you agree?
"""
class ManualClock(Clock):
    def __init__(self):
        self._t = 0.0
        self._condition = threading.Condition

    def monotonic(self) -> float:
        return self._t

    # Consumer.
    def sleep(self, secs: float) -> None:
        with self._condition:
            target = self._t + secs
            while self._t < target:
                self._condition.wait(timeout=0.001)

    # Producer.
    def advance(self, secs: float) -> None:
        with self._condition:
            self._t += secs
            self._condition.notify_all()
