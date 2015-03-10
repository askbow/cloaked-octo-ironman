from time import time, localtime, strftime
import os

def timedfile(data):
    # dump to a file for later investigation
    try:
      miltm = lambda: int(round(time()*1000000)) #microseconds
      filename = "data" + strftime("%Y%m%d%H%M%S") + str(miltm()) + ".log"
      file_dump = open(filename,"wb")
      file_dump.write(data)
      file_dump.flush()
      os.fsync(file_dump.fileno())
      file_dump.close()
    except Exception:
      pass
