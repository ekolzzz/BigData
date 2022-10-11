import time
import datetime

over_time = datetime.datetime(2022, 5, 23)
now_time = datetime.datetime.now()
result = now_time - over_time
hours = int(result.seconds / 3600)
minutes = int(result.seconds % 3600 / 60)
seconds = result.seconds%3600%60
print(f'当前时间：{over_time}')
print(f'和谭仔仔已经恋爱:{result.days}天{hours}时{minutes}分{seconds}秒')
