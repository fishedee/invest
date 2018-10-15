import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

row = 2
col = 2
n = 1
def drawPlot(title,dates,price):
	global n,row,col
	years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')
	fig = plt.subplot(row,col,n)
	n = n+1
	plt.title(title)
	fig.plot(dates, prices)
	fig.xaxis.set_major_locator(years)
	fig.xaxis.set_major_formatter(yearsFmt)
	fig.xaxis.set_minor_locator(months)
	datemin = np.datetime64(dates[0], 'Y')
	datemax = np.datetime64(dates[-1], 'Y')+ np.timedelta64(1, 'Y')
	fig.set_xlim(datemin, datemax)
	fig.format_xdata = mdates.DateFormatter('%Y-%m-%d')
	fig.grid(True)
	
plt.figure(figsize=(10,8))

dates = np.array([
	np.datetime64(datetime.datetime(2004, 5, 1),'D'),
	np.datetime64(datetime.datetime(2004, 12, 1),'D'),
	np.datetime64(datetime.datetime(2005, 6, 1),'D'),
	np.datetime64(datetime.datetime(2006, 7, 1),'D')])
print(dates,type(dates),dates.dtype)
prices = np.array([1,5,3,4])
drawPlot("demo",dates,prices)
drawPlot("demo2",dates,prices)

plt.show()