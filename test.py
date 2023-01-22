

string = 'K_0101'

from PyQt6.QtWidgets import QApplication

cCount = string.count('_')
cLen = len(string)
a = float(string[cCount+1:cLen])/10000
a2 = float(1/10000)
a3 = round((a + a2),5)
a4 = str(string[:cCount+1])+str(a3)[2:6]
print(a4)
print(str(a3)[2:6])

print(a)
print(a2)
print(a3)
print(f'{string[cCount+1:cLen]}')

'''
i = 1
while i <=4:
    cCount2 = string.count('0',cCount+i,cCount+(i+1))
    if cCount2 == 0:
        print(f'{string}, {cCount2}')
        print(f'{string[:cCount+(i+1)]}')
    i +=1
    '''





