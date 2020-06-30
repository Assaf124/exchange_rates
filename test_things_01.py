import datetime
import random
import matplotlib.pyplot as plt

# make up some data
day_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77]
date = '2018-03-12'
datetime.datetime.strptime(date, '%Y-%m-%d')
x = [datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=i) for i in range(11)]
print(x)
y = [1.2, 3.1, 0.4, 4.0, 6.05, 2.25, 5.05, 1.30, 6.45, 4.25, 2.2]
print(y)
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
# y = [i+random.gauss(0,1) for i,_ in enumerate(x)]



# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()