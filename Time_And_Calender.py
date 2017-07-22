import calendar
import time

localtime = time.localtime(time.time())
print "1 :"+str(localtime)

print "Getting formatted fonts :-"
localtime1 = time.asctime(time.localtime(time.time()))
print "2 :"+str(localtime1)

Cal_Of_Month = calendar.month(2017, 7)
print "3 :"+str(Cal_Of_Month)

# Time Methods Examples
t = time.localtime()
localtime2 = time.asctime([t])
print "4 :"+str(localtime2)


