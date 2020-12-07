from bluetooth import *
import sys

from connection import connect_port
from output import output

import busio
import digitalio
import board
import time
import numpy as np
import matplotlib.pyplot as plt

#flex sensor
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#acc gyro
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33

sock = connect_port()

#set up flex sensor
v0 = np.array([])
v1 = np.array([])
v2 = np.array([])
v3 = np.array([])
v4 = np.array([])

squareCnt = 0
triangleCnt = 0
sinCnt = 0
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#print(board)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 # create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)

#setup acc gyro
i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DS33(i2c)

accX = np.array([0])
accY = np.array([0])
accZ = np.array([0])

gyrX = np.array([0])
gyrY = np.array([0])
gyrZ = np.array([0])

v = np.array([0])
acc = np.array([])
gry = np.array([0])

diff_x=np.array([0])
diff_y=np.array([0])
8
ignore = 0
dir = ""
while True:
    v0=np.append(v0, round(chan0.voltage,2))
    v1=np.append(v1, round(chan1.voltage,2))
    v2=np.append(v2, round(chan2.voltage,2))
    v3=np.append(v3, round(chan3.voltage,2))
    v4=np.append(v4, round(chan4.voltage,2))
    
    accX = np.append(accX, round(sensor.acceleration[0],3))
    accY = np.append(accY, round(sensor.acceleration[1],3))
    accZ = np.append(accZ, round(sensor.acceleration[2],3))

    acc = np.vstack([accX,accY,accZ])

    gyrX = np.append(gyrX, round(sensor.gyro[0],3))
    gyrY = np.append(gyrY, round(sensor.gyro[1],3))
    gyrZ = np.append(gyrZ, round(sensor.gyro[2],3))
    
    diff_x = np.append(diff_x, accX[-1]-accX[-2])
    diff_y = np.append(diff_y, accY[-1]-accY[-2])

    if(len(accX)>10):
        v0 = np.delete(v0,0)
        v1 = np.delete(v1,0)
        v2 = np.delete(v2,0)
        v3 = np.delete(v3,0)
        v4 = np.delete(v4,0)
        
        accX = np.delete(accX,0)
        accY = np.delete(accY,0)
        accZ = np.delete(accZ,0)
        
        gyrX = np.delete(gyrX,0)
        gyrY = np.delete(gyrY,0)
        gyrZ = np.delete(gyrZ,0)
        
        diff_x = np.delete(diff_x,0)
        diff_y = np.delete(diff_y,0)
        
    """
    print("v0 ", v0)
    print("v1 ", v1)
    print("v2 ", v2)
    print("v3 ", v3)
    print("v4 ", v4)
    """
    
    """
    print("accX ", accX)
    print("accY ", accY)
    print("accZ ", accZ)
    
    print("gyrX ", gyrX)
    print("gyrY ", gyrY)
    print("gyrZ ", gyrZ)
    """
    v = np.vstack([v0,v1,v2,v3,v4])
    
    acc = np.vstack([accX,accY,accZ])
    
    gyr = np.vstack([gyrX,gyrY,gyrZ])
    
    time.sleep(0.1)
    #print("acc ", acc)
    
    #print("gyr ", gyr)
    print("v0 ", v0)
    #send to computer
    print(accY)
    print(diff_y[-1])
    flex=v0
    if(len(accX)==10):
    
        data = output(v, diff_x, diff_y, acc, dir, flex)
        print(dir)
        #diff_x = np.delete(diff_x,0)
        print(data)
        if ignore == 0:   
            sock.send(data)
        else:
            ignore = 0
        if data == "left":
            ignore = 1
        if data == "right":
            ignore=2
        if data[0:2] == "up":
            #ignore=3
            dir = "up"
        if data[0:4] == "down":
            #ignore=4
            dir = "down"
        if data == "dir":
            dir=""
        if data == "home":
            ignore = 4
sock.close()