
# 1.basic 
from functools import total_ordering


for nr in range(0,151,1):
    print(nr)

#2multiples of files
for nr in range(5,1000,1):
    print(nr*5)

#3counting the dojo way
def countingdojo():
    for nr in range(1,101,1):
        if nr % 5 == 0:
            print("Coding")
        if nr % 10 == 0:
            print("CodingDojo")
countingdojo()

#Whoa that sucker's huge
min=0 
max=500000
total= 0
for nr in range(min,max+1):
    if (nr % 2 != 0):
        print("{0}".format(nr))
        total=total+nr

print("sum of odd numbers from {0} ro {1}  it is {2}".format (min, max ,total) )

#Count down by Fours
def count():
    nr = 2018
    while nr > 0:
        print(nr)
        nr = nr-4

count()

#Flexible Counter
def flexible(lownum,highnum,mult):
    for nr in range(lownum,highnum):
        if nr % mult == 0 :
            print(nr)
flexible(2,9,3)

