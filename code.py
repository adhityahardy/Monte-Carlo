import math
import random

# inisiasi
total = 600 # jumlah dart
hit = 0 # jumlah dart yang dalam lingkaran
ndart = 0 # dart yang di lempar

for dart in range(total):
    Xrand = random.randint(0,1)
    Yrand = random.randint(0,1)
    ndart += 1
    if (Xrand**2)+(Yrand**2)<=1:
        hit += 1

print("total dart = "+str(total))
piTest = (hit/total)*4
print("jumlah hit = "+str(hit))
print("pi analitik = "+str(math.pi))
print("pi yang didapat = "+str(piTest))
persen = (piTest/math.pi)*100
errorpersen = abs(100-persen)
print("error = "+str(errorpersen)+" %")
