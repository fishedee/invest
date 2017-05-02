import numpy as np

def getRandomData(count):
	mean = [13, 13,13,13]
	cov = [[400, 0,0,0], [0, 400,0,0],[0,0,400,0],[0,0,0,400]]
	data = np.random.multivariate_normal(mean, cov, count)
	return data

data = getRandomData(100000)
print(np.cov(data.T),np.corrcoef(data.T))