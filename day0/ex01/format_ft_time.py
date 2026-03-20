import time
import datetime


tmp = time.time()
sc_tmp = "{:.2e}".format(tmp)
date = datetime.datetime.today()

print(f"Seconds since January 1, 1970: {format(tmp, ',.4f')} or \
      {sc_tmp} in scientific notation")
print(date.strftime("%b %d, %Y"))
