from datetime import datetime
dt = datetime.now()
favcolor = raw_input("What is your favorite color? ")

print "The date is: %s/%s/%s" % (dt.month, dt.day, dt.year)
print "The time is: %s:%s:%s" % (dt.hour, dt.minute, dt.second)
print "Your favorite color is %s." %(favcolor)