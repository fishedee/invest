import sys;
sys.path.append("..")
import source.data as data
import mystat.compare as compare

files = [
	#['../data/china_index/基本面50全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_160716_基本面50.xls'],
	#['../data/china_index/沪深300价值全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值_310398_申万菱信沪深300价值.xls'],
	#['../data/china_index/沪深300价值全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值_519671_银河沪深300价值.xls'],
	['../data/china_index/180价值全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值510030_华宝上证180价值etf.xls'],
]

for singleFile in files:
	data1 = data.readAndFilterData('../'+singleFile[0])
	data2 = data.readAndFilterData('../'+singleFile[1])
	compare.run(data1,data2)