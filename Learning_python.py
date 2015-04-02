# -*- coding: iso-8859-1 -*-
integer = 56
longinteger=2223337777887654433078
icecream = 977.235
string = "Wazzaaaaaap"
boolean = False
snapback = True

print type(integer)
print type(longinteger)
print type(icecream)
print type(string)
print type(boolean)

print boolean and snapback 
print boolean or snapback
print not boolean

int1 = 12
int2 = 69
float1 = 4.34567
float2 = 99.90

print int2/int1
print float(int2) / float(int1)
print int (float1) 
print int(snapback)

-- Tuples, lists and dictionaries --

inch = "My name is jack"
tuple1 = tuple(inch)
print tuple1

tuple2 = ('Jack', '21', 'Dundee', 'Student')
print tuple2[0]

list1 = ['Jack', '21', 'Dundee', 'Student']
print type (list1)

soccermom = [1,2,3,4,5,6,7,8,9,10]
print soccermom[0:6]
print soccermom[:5]
print soccermom [:-3]
print soccermom [-3:]

print min(soccermom)

stringylist = list ("Jack")
print ''.join(stringylist)
stringylist[4:]='ie'

l1 = [1,2,3,4,5]
print l1
del l1[2]

l1 = ['jack', 21, 'dunfermline', 'brown']
l1.append ('biochem')
l1.remove (l1[3])
l1.insert (3, 'blue')

--Dictionaries--
dictex = ({"Age":21, "Height":"6'3", "Weight":72})
print dictex 
print dictex.get("Height")
dictex.pop("Weight")

--Manipulating print-- 
strname = 'Jack'
fAge = 21
cSex = 'M'
iKids = 0
bMarried = False

print 'My name is', strname
print '%s is %.0f years old' % (strname,fAge)
print 'His sex is %c' % (cSex)
print 'He has %i children and he said it\'s %s that he is married' % (iKids, bMarried)

import math
precisionPi = int(raw_input("How precise would you like Pi to be?: "))
print 'Pi = %.*f' % (precisionPi, math.pi)

your_age = int(raw_input("How old are you?: "))

if (your_age > 10) and (your_age < 100):
    if (your_age == 21):
        print "Same here!"
    elif (your_age < 21):
        print "Awh you're just a baby..."
    else:
        print "Whoa, you're a bit older than me!"
else:
    print "Come on, don't lie about your age!"

