import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

row = 2
col = 2
n = 1

def drawPlot(title,title2,dates,price,price2):
	global n,row,col
	years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')
	fig = plt.subplot(row,col,n)
	n = n + 1
	plt.title(title+"<->"+title2)
	fig.plot(dates, price)
	fig.plot(dates, price2)
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

def filterCompareData(leftDates,leftPrices,rightDates,rightPrices):
	newDates = [];
	newLeftPrices = [];
	newRightPrices = [];
	i = 0
	j = 0
	while i < len(leftDates) and j < len(rightDates):
		if leftDates[i] < rightDates[j]:
			i = i +1 
		elif leftDates[i] > rightDates[j]:
			j = j + 1
		else:
			newDates.append(leftDates[i])
			newLeftPrices.append(leftPrices[i])
			newRightPrices.append(rightPrices[j])
			i = i + 1
			j = j + 1
	return (newDates,newLeftPrices,newRightPrices)

def runSingle(data1,data2):
	(title1,dates1,prices1) = data1
	(title2,dates2,prices2) = data2
	dates,prices1,prices2 = filterCompareData(dates1,prices1,dates2,prices2)
	newDates = [];
	for single in dates:
		newDates.append(np.datetime64(single))
	newPrices1 = np.array(prices1)
	newPrices2 = np.array(prices2)
	print("指数对比：")
	statistic(title1,newPrices1)
	statistic(title2,newPrices2)
	drawPlot(title1,title2,newDates,newPrices1,newPrices2)
	print("\n")

def run(data1,data2):
	global n
	n = 1
	for i in range(0,len(data1)):
		runSingle(data1[i],data2[i])
	plt.show()

