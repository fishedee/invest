import json
import datetime
import xlrd
import os

def readDataChinaIndex(fileAddress):
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

def readDataChinaValue(fileAddress,colName):
	source = xlrd.open_workbook(fileAddress)
	sheet = source.sheet_by_index(0)
	dates = sheet.col_values(0)[1:];
	pricesCol = -1
	iCol = 1
	while iCol < sheet.ncols:
		col = sheet.col_values(iCol)
		if col[0] == colName:
			pricesCol = iCol
			break
		iCol = iCol + 1
	if pricesCol == -1:
		raise Exception("do not find colName:["+colName+"]")
	prices = sheet.col_values(pricesCol)[1:];
	newDates = [];
	(fileDirectory,fileName) = os.path.split(fileAddress);
	(baseName,extName) = os.path.splitext(fileName);
	name = baseName.split("_")[0]
	#数据
	for single in dates:
		if single == "":
			break
		newSingle = datetime.datetime.strptime(single,'%Y-%m-%d')
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
	return (name+"_"+colName,newDates,newPrices)

def readDataChinaFund(fileAddress):
	source = xlrd.open_workbook(fileAddress)
	sheet = source.sheet_by_index(0)
	dates = sheet.col_values(0)[1:];
	pricesCol = -1
	iCol = 1
	while iCol < sheet.ncols:
		col = sheet.col_values(iCol)
		if col[0] == '复权单位净值(元)':
			pricesCol = iCol
			break
		iCol = iCol + 1
	if pricesCol == -1:
		raise Exception("do not find priceCol")
	prices = sheet.col_values(pricesCol)[1:];
	newDates = [];
	(fileDirectory,fileName) = os.path.split(fileAddress);
	(baseName,extName) = os.path.splitext(fileName);
	name = baseName.split("_")[-1]
	#数据
	for single in dates:
		if single == "":
			break
		newSingle = datetime.datetime.strptime(single,'%Y-%m-%d')
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

def readDataIndex(fileAddress):
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

def readData(fileAddress):
	fileAddressSeg = fileAddress.split("/",-1)
	folder = fileAddressSeg[3]
	if folder == "index":
		return readDataIndex(fileAddress)
	elif folder == "china_fund":
		return readDataChinaFund(fileAddress)
	elif folder == "china_index":
		return readDataChinaIndex(fileAddress)
	elif folder == "china_value":
		return readDataChinaValue("/".join(fileAddressSeg[0:-1]),fileAddressSeg[-1])
	else:
		raise Exception("unknown address")

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