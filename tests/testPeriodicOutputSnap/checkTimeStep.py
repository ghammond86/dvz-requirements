import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

#Getting time steps of outputs from H5 file
filename = "vsat_flow.h5"

with h5py.File(filename, "r+") as f:
    timeListH5 = np.empty(0, float)
    for group in f.keys():
        if 'Time' in group:
            line = group.split()
            t = float(line[1])
            timeListH5 = np.append(timeListH5, t)
    
    # print(timeList)

timeListH5 = np.sort(timeListH5)

#Get Time steps from .tec files:
nameEnd = '.tec'
timeListTec = np.empty(0,float)

runDirct = os. getcwd()

for r, dirct, files in os.walk(runDirct):
    for name in files:
        if name.endswith(nameEnd):
            fin = open(name, 'r')
            for line in fin:
                line = line.strip(' ')
                if line == []:
                    continue
                #get dimensions
                if ('T="' in line):
                    splitLine = line.split('"')
                    time = float(splitLine[1])
                    timeListTec = np.append(timeListTec, time)
timeListTec = np.sort(timeListTec)
# print(timeListTec)

#Calculate by hand timesteps to output based on .out file
fin = open('vsat_flow.out', 'r')
periodicTimestep = 5.
periodTime = 1.
individualTimes = [1.5]
finalTime = 10.

timeListOut = np.arange(0.,finalTime, periodTime)
timeListOut = np.append(timeListOut, finalTime)

for t in individualTimes:
    if t not in timeListOut:
        timeListOut = np.append(timeListOut, t)

for line in fin:
    line = line.strip(' ')
    if line == []:
        continue
    #get dimensions
    if ('Dt=' in line):
        splitLine = line.split('Step')
        words = splitLine[1].split()
        step = int(words[0])
        if step % periodicTimestep == 0:
            t = float(words[2])
            if t not in timeListOut:
                timeListOut = np.append(timeListOut, t)
            
timeListOut = np.sort(timeListOut)

maxDiffDtH5 = max(abs(timeListH5 - timeListOut))
maxDiffDtTec = max(abs(timeListTec - timeListOut))
tol = 1e-6

if maxDiffDtH5 > tol or maxDiffDtTec > tol:
    print ("Failed")
else:
    print("Passed")