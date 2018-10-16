import json
import datetime

def readData(fileAddress):
	f = open(fileAddress,'r')
	text = f.read()
	f.close()
	data = json.loads(text)
	label = data['chart_data'][0][0]['long_label']
	rawData = data['chart_data'][0][0]['raw_data']
	dates = [];
	prices = [];
	beginTime = datetime.datetime(1970,1,1,0,0,0)
	#过滤月份数据？
	for single in rawData:
		dates.append(beginTime+datetime.timedelta(milliseconds=single[0]))
		prices.append(single[1])
	return (label,dates,prices)

def getMonthLastDay(year,month):
	month = month + 1
	if month == 13:
		year = year + 1
		month = 1
	return datetime.datetime(year,month,1)-datetime.timedelta(1)

def isCloseMonth(prevDate,date):
	year = prevDate.year
	month = prevDate.month
	month = month +1
	if month == 13:
		year = year + 1
		month = 1
	return date.year == year and date.month == month

def filterData(dates,prices):
	newDates = [];
	newPrices = [];
	for i in range(0,len(dates)):
		prevDate = None
		if len(newDates) != 0:
			prevDate = newDates[-1]
		date = dates[i]
		if prevDate != None and prevDate.year == date.year and prevDate.month == date.month:
			#重复的月份数据
			newPrices[-1] = prices[i]
		else:
			if prevDate != None and isCloseMonth(prevDate,date) == False:
				raise Error("my god!")
			#非重复的月份数据
			newDates.append(getMonthLastDay(date.year,date.month))
			newPrices.append(prices[i])
	return (newDates,newPrices)

def readAndFilterData(fileAddress):
	title,dates,prices = readData(fileAddress)
	(dates,prices) = filterData(dates,prices)
	return (title,dates,prices)