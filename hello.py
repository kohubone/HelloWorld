#Author: Konstantin Sheverdyayev
#Description: a shout out to the world sensitive to tiem of the day
#Created: Sep 2019


import time

RawTime = time.localtime()#get raw time
RawHour = time.strftime("%H",RawTime) #fetch hour element only
CvtdHour = int(RawHour) #convert string to int for if

if CvtdHour >= 5 and CvtdHour < 12:
    print("Good early morning world!")
elif CvtdHour >= 12 and CvtdHour < 18:
    print("Good Afternoon world!")
elif CvtdHour >=18 and CvtdHour < 24:
    print("Good Evening world!")
else:
    print("Go home world, it's time to sleep!")

