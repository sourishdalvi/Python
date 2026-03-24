import random
import time
def getRandomDate(start, end):
 print("printing random date between", start, "and", end)
 randomgenerator= random.random()
 Dateformat= "%d/%m/%Y"
 start_time = time.mktime(time.strptime(start, Dateformat))
 end_time = time.mktime(time.strptime(end, Dateformat))
 random_time = start_time + randomgenerator * (end_time - start_time)
 randomdate = time.strftime(Dateformat, time.localtime(random_time))
 return randomdate
print("Random date is:", getRandomDate("1/1/2020", "31/12/2020"))   