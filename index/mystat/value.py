import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

row = 2
col = 2
n = 1

def drawPlot(title,dates,price):
	global n,row,col
	years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')
	fig = plt.subplot(row,col,n)
	n = n + 1
	plt.title(title)
	fig.plot(dates, price)
	fig.xaxis.set_major_locator(years)
	fig.xaxis.set_major_formatter(yearsFmt)
	fig.xaxis.set_minor_locator(months)
	datemin = np.datetime64(dates[0], 'Y')
	datemax = np.datetime64(dates[-1], 'Y')+ np.timedelta64(1, 'Y')
	fig.set_xlim(datemin, datemax)
	fig.format_xdata = mdates.DateFormatter('%Y-%m-%d')
	fig.grid(True)
	

def statistic(title,prices):
	avg = np.mean(prices,axis=0)
	median = np.median(prices,axis=0)
	minimum = np.min(prices,axis=0)
	maximum = np.max(prices,axis=0)
	current = prices[-1]
	print("指数估值：%s\n平均数: %s\n中位数: %s\n最大值: %s\n最小值: %s\n当前值：%s\n"%(title,avg,median,maximum,minimum,current))

def runSingle(data):
	(title,dates,prices) = data;
	newDates = [];
	for single in dates:
		newDates.append(np.datetime64(single))
	newPrices = np.array(prices)
	statistic(title,newPrices)
	drawPlot(title,newDates,newPrices)

def run(data):
	global n
	n = 1
	for singleData in data:
		runSingle(singleData)
	plt.show()

