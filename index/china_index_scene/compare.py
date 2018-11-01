import sys;
sys.path.append("..")
import source.data as data
import mystat.compare as compare

files = [
	#['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/中证红利全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50_交易特征_时间序列分析.xls','../data/china_index/上证50全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/中证红利全收益_交易特征_时间序列分析.xls','../data/china_index/基本面50全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/基本面50全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/上证红利全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/中证红利全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50_交易特征_时间序列分析.xls','../data/china_index/中证500全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/中证500全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300低波全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300价值全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300成长全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500低波全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500价值全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_index/中证500成长全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/180价值全收益_交易特征_时间序列分析.xls'],
	#['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_index/180成长全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/180价值全收益_交易特征_时间序列分析.xls','../data/china_index/沪深300价值全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/180价值全收益_交易特征_时间序列分析.xls','../data/china_index/中证500价值全收益_交易特征_时间序列分析.xls'],
	['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_index/中证500价值全收益_交易特征_时间序列分析.xls'],

]

for singleFile in files:
	data1 = data.readAndFilterData('../'+singleFile[0])
	data2 = data.readAndFilterData('../'+singleFile[1])
	compare.run(data1,data2)