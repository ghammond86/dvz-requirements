import numpy as np

dtList = []
initialDt = 1e-3
maxDt = 1.0
finalT = 10.0
dt = initialDt
tol = 1e-6

t = dt
dtManual = []
dtManual.append(dt)
while abs(t-finalT) > tol:
    dt *= 2.0
    if dt > maxDt:
        dt = maxDt
    if dt+t > finalT:
        dt = finalT - t
    dtManual.append(dt)
    t += dt

fin = open('vsat_flow.out', 'r')

for line in fin:
    line = line.strip()
    if line == []:
        continue
    #get dimensions
    if ('Dt=' in line):
        splitLine = line.split('Dt=')
        words = splitLine[1].split()
        dtList.append(float(words[0]))

dtManual = np.array(dtManual)
dtList = np.array(dtList)

maxDiffDt = max(abs(dtManual - dtList))

if maxDiffDt > tol:
    print ("Failed")
else:
    print("Passed")