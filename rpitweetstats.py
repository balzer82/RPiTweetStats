#!/usr/bin/env python
import os
import sys
import tweepy
import time

from datetime import timedelta


# Uptime
# http://planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way
with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds = uptime_seconds))


# CPU Usage
# http://ubuntuforums.org/showthread.php?t=148781
TIMEFORMAT = "%m/%d/%y %H:%M:%S"
INTERVAL = 2

def getTimeList():
    statFile = file("/proc/stat", "r")
    timeList = statFile.readline().split(" ")[2:6]
    statFile.close()
    for i in range(len(timeList))  :
        timeList[i] = int(timeList[i])
    return timeList

def deltaTime(interval)  :
    x = getTimeList()
    time.sleep(interval)
    y = getTimeList()
    for i in range(len(x))  :
        y[i] -= x[i]
    return y

dt = deltaTime(INTERVAL)
timeStamp = time.strftime(TIMEFORMAT)
cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))


# Twitter
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# CPU Temp
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]



# Fire the Tweet
message = '[Bot]: CPU ' + temp + unichr(176) + 'C, ' + str('%.1f' %cpuPct) + '% Load. Uptime: ' + uptime

try:
     print 'Tweet: ' + message
     api.update_status(message)
except Exception, e:
     print 'Fehler:', e
