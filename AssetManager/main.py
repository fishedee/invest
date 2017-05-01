import numpy as np
import math

year = 100
count = 100000

def getRandomData(count):
	mean = [13, 8]
	cov = [[400, 72], [72, 144]]
	data = np.random.multivariate_normal(mean, cov, count)
	return data

def balanceByDistance(obond,oshare):
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,2)

	result = []
	for testCase in meanData:
		bond = obond
		share = oshare
		for testYear in testCase:
			mshare = share
			mbond = bond
			share *= 1+testYear[0]/100
			bond *= 1+testYear[1]/100
			if mbond != 0 and mshare != 0 and math.fabs(share/bond-mshare/mbond)/(mshare/mbond)>0.15:
				total = share + bond
				share = total*oshare/(oshare+obond)
				bond = total*obond/(oshare+obond)
		singleResult = (bond+share)/(obond+oshare)
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)

def balanceByThink(obond,oshare):
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,2)

	result = []
	for testCase in meanData:
		bond = obond
		share = oshare
		mbond = obond
		mshare = oshare
		for testYear in testCase:
			share *= 1+testYear[0]/100
			bond *= 1+testYear[1]/100
			total = share + bond
			mshare *= 1.13
			mbond *= 1.08
			share = total*mshare/(mshare+mbond)
			bond = total*mbond/(mshare+mbond)
		singleResult = (bond+share)/(obond+oshare)
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)

def balance(obond,oshare):
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,2)

	result = []
	for testCase in meanData:
		bond = obond
		share = oshare
		for testYear in testCase:
			share *= 1+testYear[0]/100
			bond *= 1+testYear[1]/100
			total = share + bond
			share = total*oshare/(oshare+obond)
			bond = total*obond/(oshare+obond)
		singleResult = (bond+share)/(obond+oshare)
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)


def origin(obond,oshare):
	meanData = getRandomData(year*count)
	meanData = meanData.reshape(count,year,2)

	result = []
	for testCase in meanData:
		bond = obond
		share = oshare
		for testYear in testCase:
			share *= 1+testYear[0]/100
			bond *= 1+testYear[1]/100
		singleResult = (bond+share)/(obond+oshare)
		singleResult = (pow(singleResult,1/year)-1)*100
		result.append(singleResult)
	return np.mean(result),np.std(result)

data = getRandomData(100000)
print(np.mean(data,axis=0),np.cov(data.T),np.corrcoef(data.T))

for i in range(0,11,1):
	obond = float(i)
	oshare = float(10-i)
	mean,var = balanceByDistance(obond,oshare)
	sharp = mean/var
	print("bond:%d,share:%d,result:%f,%f,%f"%(obond,oshare,mean,var,sharp))


