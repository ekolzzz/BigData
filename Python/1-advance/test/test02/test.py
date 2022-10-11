# import time
# import datetime
# # # 获取代码执行时间的当前时间
# over_time = datetime.datetime(2022, 5, 23)
# now_time = datetime.datetime.now()
# time_str = now_time - over_time
#
# print(time_str)
import datetime

""" 2022/02/28 --> 2022-02-28 """
start_date = '2022/02/28'
middle = datetime.datetime.strptime('2022/02/28', '%Y/%m/%d')
end_date = datetime.datetime.strftime(middle, "%Y-%m-%d")
print(end_date)