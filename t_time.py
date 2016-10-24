import datetime
import time


now_time = datetime.datetime.now()
print now_time, type(now_time)
print time.localtime()
yes_time = now_time + datetime.timedelta(days=-1)
print yes_time
yes_time_nyr = yes_time.strftime('%Y-%m-%d')
print yes_time_nyr
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print time.strftime('%Y-%m-%d %H:%M:%S')
print time.strftime('%Y')
print time.strftime('%d/%b/%Y:%H:%M:%S',time.localtime())
print time.strftime('%d/%b/%Y',time.localtime())

print time.strftime('%Y%m%d%H%M%S',time.localtime())


print time.strftime('%Y-%m-%d %H:%M:%S')


print time.strftime('%Y%m%d')

print "a"

def _gen_week_timestamp():
        """
        generate last week timestamp 
        Return:
            (1452441600.0, 1453046399.9)
        """
        now_time = datetime.datetime.now()
        end_day = -now_time.weekday()
        start_day = end_day - 7
        week_end = now_time + datetime.timedelta(days=end_day)
        week_start = now_time + datetime.timedelta(days=start_day)
        format_str = '%Y-%m-%d'
        week_start = week_start.strftime(format_str)
        week_end = week_end.strftime(format_str)
        ts_start = time.mktime(time.strptime(week_start, format_str))
        ts_end = time.mktime(time.strptime(week_end, format_str))
        return ts_start, ts_end - 0.1
print _gen_week_timestamp()
