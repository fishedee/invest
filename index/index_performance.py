import source.data as data
import mystat.performance as performance

files = [
	'../data/index/s&p/^SPX',
	'../data/index/s&p/^SPXTR',
	'../data/index/s&p/^MID',
	'../data/index/s&p/^SML',
	'../data/index/nasdaq/^IXIC',
	'../data/index/nasdaq/^NACTR',
	'../data/index/nasdaq/^NDX',
	'../data/index/nasdaq/^NA100TR',
	'../data/index/russell/^RUT200',
	'../data/index/russell/^RUT200TR',
	'../data/index/russell/^RUI',
	'../data/index/russell/^RUITR',
	'../data/index/russell/^RUT',
	'../data/index/russell/^RUTTR',
	'../data/index/msci/^MSEAFEACAP',
	'../data/index/msci/^MSEFACTR',
	'../data/index/msci/^MSEAFELCAP',
	'../data/index/msci/^MSEFLCTR',
	'../data/index/msci/^MSEAFEMCAP',
	'../data/index/msci/^MSEFMCTR',
	'../data/index/msci/^MSEAFEUCAP',
	'../data/index/msci/^MSEFUCTR',
]

for singleFile in files:
	data1 = data.readAndFilterData(singleFile)
	performance.run(data1)