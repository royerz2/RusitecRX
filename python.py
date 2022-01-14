import numpy as np
import serial
import pandas as pd
import csv
import os
import time
import xlsxwriter

try:
    ser = serial.Serial('/dev/cu.usbserial-1410', 9600, timeout=5)
except serial.serialutil.SerialException:
    try:
        ser = serial.Serial('/dev/cu.usbserial-1420', 9600, timeout=5)
    except serial.serialutil.SerialException:
        try:
            ser = serial.Serial('/dev/cu.usbserial-14210', 9600, timeout=5)
        except serial.serialutil.SerialException:
            ser = serial.Serial('/dev/cu.usbmodem14201', 9600, timeout=5)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d/%m/%Y-%H:%M:%S", named_tuple)

with open('./sensor1.csv', 'r+') as csvfile:
    sensor1 = csv.writer(csvfile, delimiter=',',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)

    sensor1.writerow(['methane', 'hydrogen', 'temperature', 'humidity', 'time'])


with open('./sensor2.csv', 'r+') as csvfile:
    sensor2 = csv.writer(csvfile, delimiter=',',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)

    sensor2.writerow(['methane', 'hydrogen', 'temperature', 'humidity', 'time'])

# read from Arduino
input_str = ser.readline()
print ("Read input" + input_str.decode ("utf-8").strip() + " from Arduino")

d = {'methane', 'hydrogen', 'temperature', 'humidity'}

df = pd.DataFrame(data=d)

while 1:
    time_string = time.strftime("%d/%m/%Y-%H:%M:%S", named_tuple)
    input_str = ser. readline().decode("utf-8").strip()
    print(input_str)
    input_list = input_str.split(",")
    print(input_list)

    if input_list[4] == " 1":

        with open('sensor1.csv', 'a') as csvfile:

            data_df = csv.writer(csvfile)

            data_df.writerow([input_list[0], input_list[1], input_list[2],
                              input_list[3], time_string])

            print("Data Addition Completed")

    elif input_list[4] == " 2":

        with open('sensor2.csv', 'a') as csvfile:

            data_df = csv.writer(csvfile)

            data_df.writerow([input_list[0], input_list[1], input_list[2],
                              input_list[3], time_string])

            print("Data Addition Completed")
