import datetime
import time
a=time.time()
b= datetime.datetime.fromtimestamp(a).isoformat() + 'Z'
print(a)
print(b)

