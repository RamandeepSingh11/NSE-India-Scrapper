import unittest,sys,datetime
sys.path.insert(0,'..')
from NSE.companies import Companies
print(Companies().HistoricalData('RBLBANK',Series=[Companies().EQ,Companies().RL],TimePeriod='1y'))