import source.data as data
import mystat.corrcoef as corrcoef

files = [
	['../data/index/s&p/^SPX','../data/index/s&p/^MID'],
	['../data/index/s&p/^SPX','../data/index/s&p/^SML'],
	['../data/index/s&p/^MID','../data/index/s&p/^SML'],
	['../data/index/s&p/^SPX','../data/index/nasdaq/^IXIC'],
	['../data/index/s&p/^SPXTR','../data/index/nasdaq/^NA100TR'],
	['../data/index/russell/^RUT200TR','../data/index/russell/^RUITR'],
	['../data/index/russell/^RUT200TR','../data/index/russell/^RUTTR'],
	['../data/index/russell/^RUITR','../data/index/russell/^RUTTR'],
	['../data/index/msci/^MSEFACTR','../data/index/msci/^MSEFLCTR'],
	['../data/index/msci/^MSEFLCTR','../data/index/msci/^MSEFMCTR'],
	['../data/index/msci/^MSEFLCTR','../data/index/msci/^MSEFUCTR'],
	['../data/index/s&p/^SPXTR','../data/index/msci/^MSEFLCTR'],
]

for singleFile in files:
	data1 = data.readAndFilterData(singleFile[0])
	data2 = data.readAndFilterData(singleFile[1])
	corrcoef.run(data1,data2)