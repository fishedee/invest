import sys;
sys.path.append("..")
import source.data as data
import mystat.compare as compare

files = [
	['../data/china_index/上证红利全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_510880_上证红利etf.xls'],
	['../data/china_index/上证50全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_510050_上证50etf.xls'],
	['../data/china_index/基本面50全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_160716_基本面50.xls'],
	['../data/china_index/中证红利全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_090010_大成中证红利.xls'],
	['../data/china_index/中证红利全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_161907_万家中证红利.xls'],
	['../data/china_index/中证红利全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_100032_富国红利增强.xls'],
	['../data/china_index/沪深300全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_510300_沪深300etf.xls'],
	['../data/china_index/中证500全收益_交易特征_时间序列分析.xls','../data/china_fund/每日基金净值与行情_510500_中证500etf.xls'],
]

for singleFile in files:
	data1 = data.readAndFilterData('../'+singleFile[0])
	data2 = data.readAndFilterData('../'+singleFile[1])
	compare.run(data1,data2)