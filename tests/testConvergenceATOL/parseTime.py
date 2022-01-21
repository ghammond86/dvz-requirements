dtList = []

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

print(dtList)