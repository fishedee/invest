import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import data

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

def statistic(title,prices):
	allEarning = prices[-1]/prices[0]
	monthCount = prices.shape[0]
	priceInc = prices[0:-1]/prices[1:]
	monthAvg = np.mean(priceInc,axis=0)
	yearAvg = monthAvg*12
	variance = np.std(priceInc,axis=0)
	monthCompound = pow(allEarning,1.0/(monthCount-1))-1
	yearCompound = pow(monthCompound+1,12)
	print("指数：%s\n统计月份：%d\n总收益：%f\n月平均收益率：%f\n年平均收益率：%f\n月波动率：%f\n月复合收益率：%f\n年复合收益率：%f\n"%(title,monthCount,allEarning,monthAvg,yearAvg,variance,monthCompound,yearCompound))

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

def handleSingle(fileAddress,fileAddress2):
	title1,dates1,prices1 = data.readAndFilterData(fileAddress)
	title2,dates2,prices2 = data.readAndFilterData(fileAddress2)
	dates,prices1,prices2 = filterCompareData(dates1,prices1,dates2,prices2)
	newDates = [];
	for single in dates:
		newDates.append(np.datetime64(single))
	newPrices1 = np.array(prices1)
	newPrices2 = np.array(prices2)
	print("指数对比：")
	statistic(title1,newPrices1)
	statistic(title2,newPrices2)
	newPrices1 = newPrices1/newPrices1[0]
	newPrices2 = newPrices2/newPrices2[0]
	drawPlot(title1,title2,dates,newPrices1,newPrices2)
	print("\n")

files = [
	['../data/china_index/上证50_交易特征_时间序列分析.xls','../data/china_index/上证50全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/基本面50全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/上证50_交易特征_时间序列分析.xls','../data/china_index/上证红利全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/上证50_交易特征_时间序列分析.xls','../data/china_index/中证红利全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/中证500全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300低波全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300价值全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300成长全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500低波全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500价值全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500成长全收益_交易特征_时间序列分析.xls'],
]

for singleFile in files:
	handleSingle(singleFile[0],singleFile[1])


