import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import data

def drawPlot(title,dates,price):
	years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')
	fig, ax = plt.subplots()
	plt.title(title)
	ax.plot(dates, price)
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

def handleSingle(fileAddress):
	title,dates,prices = data.readAndFilterData(fileAddress)
	newDates = [];
	for single in dates:
		newDates.append(np.datetime64(single))
	newPrices = np.array(prices)
	statistic(title,newPrices)
	drawPlot(title,newDates,newPrices)

files = [
	'../data/china_fund/每日基金净值与行情_510050_上证50etf.xls',
	'../data/china_fund/每日基金净值与行情_160716_基本面50.xls',
	'../data/china_fund/每日基金净值与行情_510300_沪深300etf.xls',
	'../data/china_fund/每日基金净值与行情_510500_中证500etf.xls',
	'../data/china_fund/每日基金净值与行情_510880_上证红利etf.xls',
	'../data/china_fund/每日基金净值与行情_501029_标普红利.xls',
	'../data/china_fund/每日基金净值与行情_161907_万家中证红利.xls',
	'../data/china_fund/每日基金净值与行情_100032_富国红利增强.xls',
	'../data/china_fund/每日基金净值与行情_090010_大成中证红利.xls',
]

for singleFile in files:
	handleSingle(singleFile)

