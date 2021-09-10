import numpy as np

dtList = []
initialDt = 1.0
minDt = 0.001
finalT = 10.0
dt = initialDt
tol = 1e-6
ncut = 0
maxCut = 5

t = dt
dtManual = []
while ncut < maxCut :
    dt /= 2.0
    if dt < minDt:
        break
    dtManual.append(dt)
    ncut += 1

fin = open('output.txt', 'r')

for line in fin:
    line = line.strip()
    if line == []:
        continue
    #get dimensions
    if ('dt=' in line):
        splitLine = line.split('dt=')
        words = splitLine[1].split()
        dtList.append(float(words[0]))

dtManual = np.array(dtManual)
dtList = np.array(dtList)

maxDiffDt = max(abs(dtManual - dtList))

if maxDiffDt > tol:
    print ("Failed")
else:
    print("Passed")