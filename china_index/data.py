import datetime
import xlrd
import os

def readData(fileAddress):
	source = xlrd.open_workbook(fileAddress)
	sheet = source.sheet_by_index(0)
	dates = sheet.col_values(0)[1:];
	prices = sheet.col_values(3)[1:];
	newDates = [];
	(fileDirectory,fileName) = os.path.split(fileAddress);
	(baseName,extName) = os.path.splitext(fileName);
	name = baseName.split("_")[0]
	#数据
	for single in dates:
		if single == "":
			break
		newSingle = datetime.datetime(1899,12,30,1,0,0)+datetime.timedelta(days=single)
		newDates.append(newSingle)
	newPrices = [];
	for single in prices:
		if single == "":
			break
		newPrices.append(single)
	if len(newDates) != len(newPrices):
		raise Exception("my god")
	newDates.reverse()
	newPrices.reverse()
	return (name,newDates,newPrices)

def getMonthLastDay(year,month):
	month = month + 1
	if month == 13:
		year = year + 1
		month = 1
	return datetime.datetime(year,month,1)-datetime.timedelta(1)

def nextMonth(prevDate):
	year = prevDate.year
	month = prevDate.month
	month = month +1
	if month == 13:
		year = year + 1
		month = 1
	return getMonthLastDay(year,month)

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
			if prevDate != None:
				nextDate = nextMonth(prevDate)
				while nextDate.year != date.year or nextDate.month != date.month:
					newDates.append(getMonthLastDay(nextDate.year,nextDate.month))
					newPrices.append(prices[-1])
					nextDate = nextMonth(nextDate)
			#非重复的月份数据
			newDates.append(getMonthLastDay(date.year,date.month))
			newPrices.append(prices[i])
	return (newDates,newPrices)

def readAndFilterData(fileAddress):
	title,dates,prices = readData(fileAddress)
	(dates,prices) = filterData(dates,prices)
	return (title,dates,prices)