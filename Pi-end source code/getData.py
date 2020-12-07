import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import numpy as np
import matplotlib.pyplot as plt
 
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
 
 


    
while True:
    v0=np.append(v0, round(chan0.voltage,2))
    v1=np.append(v1, round(chan1.voltage,2))
    v2=np.append(v2, round(chan2.voltage,2))
    v3=np.append(v3, round(chan3.voltage,2))
    v4=np.append(v4, round(chan4.voltage,2))
    if(len(v1)>10):
        v0 = np.delete(v0,0)
        v1 = np.delete(v1,0)
        v2 = np.delete(v2,0)
        v3 = np.delete(v3,0)
        v4 = np.delete(v4,0)
    print("v0 ", v0)
    print("v1 ", v1)
    print("v2 ", v2)
    print("v3 ", v3)
    print("v4 ", v4)
    
    

