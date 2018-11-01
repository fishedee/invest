import sys;
sys.path.append("..")
import source.data as data
import mystat.value_compare as value_compare

files = [
	#['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/基本面50_财务特征_时间序列分析.xls'],
	#['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/沪深300_财务特征_时间序列分析.xls'],
	#['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/中证500_财务特征_时间序列分析.xls']
	#['../data/china_value/中证红利_财务特征_时间序列分析.xls','../data/china_value/基本面50_财务特征_时间序列分析.xls'],
	#['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/上证红利_财务特征_时间序列分析.xls'],
	#['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/中证红利_财务特征_时间序列分析.xls'],
	#['../data/china_value/沪深300_财务特征_时间序列分析.xls','../data/china_value/上证红利_财务特征_时间序列分析.xls'],
	#['../data/china_value/沪深300_财务特征_时间序列分析.xls','../data/china_value/中证红利_财务特征_时间序列分析.xls']
	#['../data/china_value/沪深300_财务特征_时间序列分析.xls','../data/china_value/沪深300价值_财务特征_时间序列分析.xls'],
	#['../data/china_value/沪深300_财务特征_时间序列分析.xls','../data/china_value/沪深300成长_财务特征_时间序列分析.xls'],
	#['../data/china_value/中证500_财务特征_时间序列分析.xls','../data/china_value/中证500价值_财务特征_时间序列分析.xls'],
	#['../data/china_value/中证500_财务特征_时间序列分析.xls','../data/china_value/中证500成长_财务特征_时间序列分析.xls'],
	['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/180价值_财务特征_时间序列分析.xls'],
	['../data/china_value/上证50_财务特征_时间序列分析.xls','../data/china_value/180成长_财务特征_时间序列分析.xls'],

]

for singleFile in files:
	indicate = ['市盈率','市净率','净资产收益率[%]','总市值[亿]'];
	result1 = [];
	result2 = [];
	for singleIndicate in indicate:
		singleResult1 = data.readAndFilterData('../'+singleFile[0]+'/'+singleIndicate)
		singleResult2 = data.readAndFilterData('../'+singleFile[1]+'/'+singleIndicate)
		result1.append(singleResult1)
		result2.append(singleResult2)
	value_compare.run(result1,result2)