import datetime
import time

# Get the current time
x = datetime.datetime.now()

# Get Unix timestamp (seconds since Jan 1, 1970)
timestamp = time.time()

print(f"Seconds since January 1, 1970: {int(timestamp):,} or {timestamp:.2e} in scientific notation")
print(f"{x.strftime('%b %d %Y')}")
