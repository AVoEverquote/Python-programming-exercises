import math

C = 50.0
H = 30.0

D = raw_input()

inputArr = D.split(',')
ansList = []
for num in inputArr:
    ansList.append(int(round(math.sqrt(((2.0 * C * float(num))/H)))))

print str(ansList)[1:-1]
