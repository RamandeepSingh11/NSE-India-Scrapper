import unittest,sys,datetime
sys.path.insert(0,'..')
from NSE.companies import Companies
print(Companies().HistoricalData('RBLBANK',Series=[r'%22EQ%22',r'%22RL%22'],TimePeriod='1y'))