import numpy as np
import math

n = 4
year = 100
count = 100000

def getRandomData(count):
	mean = [13, 13,13,13]
	cov = [[400, 0,0,0], [0, 400,0,0],[0,0,400,0],[0,0,0,400]]
	data = np.random.multivariate_normal(mean, cov, count)
	return data

def balance():
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,n)

	result = []
	for testCase in meanData:
		perResult = [1.0,1.0,1.0,1.0]
		for testYear in testCase:
			tempSingle = 0
			for index in range(0,n):
				perResult[index] *= 1+testYear[index]/100
				tempSingle += perResult[index]
			for index in range(0,n):
				perResult[index] = tempSingle/n
		temp = 0
		for index in range(0,n):
			temp += perResult[index]
		singleResult = temp/n
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)

def origin():
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,n)

	result = []
	for testCase in meanData:
		perResult = [1.0,1.0,1.0,1.0]
		for testYear in testCase:
			for index in range(0,n):
				perResult[index] *= 1+testYear[index]/100
		temp = 0
		for index in range(0,n):
			temp += perResult[index]
		singleResult = temp/n
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)

allTest = [origin,balance]

for index,singleTest in enumerate(allTest):
	mean,var = singleTest()
	sharp = mean/var
	print("result%d:%f,%f,%f"%(index,mean,var,sharp))