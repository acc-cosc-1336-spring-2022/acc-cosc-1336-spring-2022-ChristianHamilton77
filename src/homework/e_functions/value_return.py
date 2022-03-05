#Your task is to use the modulus(%) operator to calculate the seconds, minutes, and hours given the total seconds since 1970. 
import time
from datetime import date
def time_current(time = time.time()):
    hours = (time / 3600) % 24
    minutes = (hours % 1) * 60
    seconds = (minutes % 1) * 60
    # print("Epoch Since 1970: "+str(time))
    # print("Todays Hour: "+str(int(hours)))
    # print("Todays Minutes: "+str(int(minutes)))
    # print("Todays Seconds: "+str(int(seconds)))
    #print("Time = "+str(int(hours))+":"+str(int(minutes))+":"+str(int(seconds))+" (GMT)")
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    return hours, minutes, seconds
#print(time_current()[0])

def get_hour(epoch_seconds=time.time()):#get_hour takes an epoch_seconds parameter
    hour = int((epoch_seconds / 3600) % 24)
    return hour
#print(get_hour())

def get_minutes(epoch_seconds=time.time()):#get_minutes takes an epoch_seconds parameter
    hour = (epoch_seconds / 3600) % 24
    minutes = int((hour % 1) * 60)
    return minutes
#print(get_minutes())

def get_seconds(epoch_seconds=time.time()):#get_seconds takes an epoch_seconds parameter
    hour = (epoch_seconds / 3600) % 24
    minutes = (hour % 1) * 60
    seconds = int((minutes % 1) * 60)
    return seconds
#print(get_seconds())

def time_from_utc(utc_offset,utc_zero):##Create a value return function time_from_utc that accepts two parameters utc_offset and utc_zero. Sum utc_offset and utc_zero.
    sum = utc_offset + utc_zero
    return sum % 24


def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes  = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridiem

    return  time