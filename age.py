# -*- coding: iso-8859-1 -*-
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

