import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def drawPlot(title,title2,dates,price,price2):
	years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')
	fig, ax = plt.subplots()
	plt.title(title+"<->"+title2)
	ax.plot(dates, price)
	ax.plot(dates,price2)
	ax.xaxis.set_major_locator(years)
	ax.xaxis.set_major_formatter(yearsFmt)
	ax.xaxis.set_minor_locator(months)
	datemin = np.datetime64(dates[0], 'Y')
	datemax = np.datetime64(dates[-1], 'Y')+ np.timedelta64(1, 'Y')
	ax.set_xlim(datemin, datemax)
	ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
	ax.grid(True)
	fig.autofmt_xdate()
	plt.show()

def statistic(title,title2,prices,prices2):
	print("指数：%s<->%s\n相关性：%f\n"%(title,title2,np.corrcoef(prices,prices2)[0,1]))

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

def run(data1,data2):
	(title1,dates1,prices1) = data1
	(title2,dates2,prices2) = data2
	dates,prices1,prices2 = filterCompareData(dates1,prices1,dates2,prices2)
	newDates = [];
	for single in dates:
		newDates.append(np.datetime64(single))
	newPrices1 = np.array(prices1)
	newPrices2 = np.array(prices2)
	print("指数对比：")
	statistic(title1,title2,newPrices1,newPrices2)
	newPrices1 = newPrices1[0:-1]/newPrices1[1:]
	newPrices2 = newPrices2[0:-1]/newPrices2[1:]
	drawPlot(title1,title2,dates[1:],newPrices1,newPrices2)
	print("\n")



