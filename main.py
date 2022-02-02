#!/usr/bin/python
import datetime
now = datetime.datetime.now()

print("Hi EP this job with python runs each minute...")

f = open("app/logs/app_logs.txt", "w")
f.write("Now the file has more content!")
f.close()