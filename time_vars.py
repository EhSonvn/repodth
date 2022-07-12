import pytz
from datetime import datetime
import time

class time_var:
    my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
    
    date_rn = my_time.strftime("%d")

    month_rn = my_time.strftime("%m")

    year_rn = my_time.strftime("%Y")

    ts = datetime.fromtimestamp(time.time()+25200).strftime('%H:%M:%S')
