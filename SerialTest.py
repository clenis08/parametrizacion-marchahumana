import serial  # Import Serial Library
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import re
import threading
Y=0
X=0
gDataX = []
gDataY = []
gDataX.append([0.0])
gDataX.append([0.0])
gDataY.append([0.0])
gDataY.append([0.0])



def getData(out_dataX,out_dataY):
    with serial.Serial('com5', 115200,timeout=1) as ser: # Create Serial port object called arduinoSerialData
        while True:
                line= ser.readline().decode('utf-8')  # read a '\n' terminated line
                try:
                    if "Y" in line:
                        Y = float(line[1:len(line)])
                    if "X" in line:
                        X = float(line[1:len(line)])
                    #print(type(X))
                    out_dataY[1].append(Y)
                    out_dataX[1].append(X)
                    if len(out_dataX[1]) > 200:
                        out_dataX[1].pop(0)
                    if len(out_dataY[1]) > 200:
                        out_dataY[1].pop(0)
                    #print(out_dataX[1])
                    #print(out_dataY[1])
                except:
                    pass
dataCollector = threading.Thread(target = getData, args=(gDataX,gDataY, ))
dataCollector.start()

def update_line(num,hl,data):
    dx = np.array(range(len(data[1])))
    dy = np.array(data[1])
    hl.set_data(dx,dy)
    return hl,
def update_lineY(num,hlY,data):
    dx = np.array(range(len(data[1])))
    dy = np.array(data[1])
    hlY.set_data(dx, dy)
    return hlY,

fig=plt.figure(figsize=(10,8))
plt.xlim(0,200)
plt.ylim(0,1023)
hl,=plt.plot(gDataX[1],gDataX[1])
hlY,=plt.plot(gDataY[1],gDataY[1])

line_aniX = animation.FuncAnimation(fig, update_line, fargs=(hl, gDataX),
                                       interval=50, blit=False)

line_aniY = animation.FuncAnimation(fig, update_lineY, fargs=(hlY, gDataY),
                                       interval=50, blit=False)
plt.show()
dataCollector.join()