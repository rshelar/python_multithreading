import time
from datetime import datetime, timedelta

"""
time.time()
	•	Returns seconds since the Unix epoch (Jan 1, 1970, UTC).
	•	Float with fractional seconds.
"""
print(time.time())

"""
datetime.now()
	•	Human-readable current time.
	•	Naive or timezone-unaware datetime.  local wall-clock time (your system’s local timezone),
"""
print(datetime.now())
print(f"Time zone: {datetime.now().tzinfo}")

"""
time.monotonic()
	•	Monotonic (never goes backwards).
	•	Returns float seconds from an unspecified start point.
"""
start = time.monotonic()
time.sleep(1)
end = time.monotonic()
elapsed = end - start
print(f"Start: {start}, End: {end}, Elapsed: {elapsed}")


"""
time.sleep(secs)
	•	Block the thread for given seconds.
	•	Uses wall-clock time under the hood.
"""
time.sleep(1)

"""
Date/Time with datetime and timedelta
	•	datetime for human-readable points in time.
	•	timedelta for differences in time.
"""
now = datetime.now()
future = now + timedelta(seconds=10)
diff = future - now
print(f"Now: {now}, Future: {future}, Diff: {diff.seconds} secs")

"""
ISO Format:
Date only: YYYY-MM-DD
Date and time: YYYY-MM-DDTHH:MM:SS
Date and time with fractional seconds: YYYY-MM-DDTHH:MM:SS.ssssss 
 
"""
date1 = "2025-09-01T09:55:40"
date2 = "2025-09-10T21:15:20"
d1 = datetime.fromisoformat(date1)
d2 = datetime.fromisoformat(date2)
diff = d2 - d1
print(f"D1: {d1}, D2: {d2}, Diff: {diff.days} days or {diff.seconds} secs")

t1 = datetime.now()
t2 = datetime.now() + timedelta(minutes=10)
diff = t2 - t1
print(f"Diff: {diff.seconds} seconds")