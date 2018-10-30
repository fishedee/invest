import sys;
sys.path.append("..")
import source.data as data
import mystat.value as value

files = [
	'../data/china_value/上证50_财务特征_时间序列分析.xls',
	'../data/china_value/基本面50_财务特征_时间序列分析.xls',
]

for singleFile in files:
	indicate = ['市盈率','市净率','净资产收益率[%]','总市值[亿]'];
	result = [];
	for singleIndicate in indicate:
		singleResult = data.readAndFilterData('../'+singleFile+'/'+singleIndicate)
		result.append(singleResult)
	value.run(result)