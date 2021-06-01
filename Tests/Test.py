import unittest,sys,datetime
sys.path.insert(0,'..')
from NSE.companies import Companies
from NSE.derivatives import Derivatives
from NSE.equitySMEMarket import EquitySMEMarket
from NSE.indices import Indices
from NSE.preOpenMarket import PreOpenMarket
from NSE import ValidSymbols
Sample_Company="RBLBANK"
Series=[ValidSymbols['COMPANIES']['EQ'],ValidSymbols['COMPANIES']['RL']]
class TestNSE(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.companies=Companies()
		cls.equitySMEMarket=EquitySMEMarket()
		cls.deriatives=Derivatives()
		cls.indices=Indices()
		cls.preOpenMarket=PreOpenMarket()
	def test_init(self):
		self.assertRaises(ValueError,Companies,-1)
	def test_Company(self):
		results=self.companies.GetPriceInfo(Sample_Company)
		self.assertGreaterEqual(len(results),5)
		self.assertEqual(results['info']['symbol'],Sample_Company)
		results=self.companies.GetTradeInfo(Sample_Company)
		self.assertGreaterEqual(len(results),4)
		results=self.companies.HistoricalData(Sample_Company,Series,'1m')
		self.assertGreaterEqual(len(results),2)
		self.assertEqual(results['meta']['symbols'][0],'RBLBANK')
		self.assertEqual(results['meta']['series'],['EQ','RL'])
		self.assertGreaterEqual(len(results['data']),0)
		self.assertRaises(ValueError,self.companies.HistoricalData,Sample_Company,Series,TimePeriod='1e')
		self.assertRaises(ValueError,self.companies.HistoricalData,Sample_Company,Series,Start='2021-04-2021',End='06-02-2021')
		self.assertRaises(ValueError,self.companies.HistoricalData,Sample_Company,Series,TimePeriod=['1'])
		self.assertRaises(Exception,self.companies.HistoricalData,Sample_Company,Series,Start=12,End=23)
		#Getting Data For Future Dates
		self.assertRaises(Exception,self.companies.HistoricalData,Sample_Company,Series,Start='20-07-2022',End='20-05-2025')
	def test_derivatives(self):
		results=self.deriatives.EquityDerivatives(self.deriatives.TOP20CONTRACTS)
		self.assertEqual(len(results),3)
		self.assertEqual(len(results['data']),20)
		results=self.deriatives.EquityDerivatives(self.deriatives.NIFTY50OPTIONS)
		self.assertGreaterEqual(len(results['data']),50)
		# self.assertRaises(RuntimeError,self.deriatives.EquityDerivatives,'sdsfsd')
		self.assertRaises(ValueError,self.deriatives.EquityDerivatives,self.deriatives.ALLINRCONTRACTS)
		self.assertGreaterEqual(len(self.deriatives.CurrencyDerivatives(self.deriatives.ALLINRCONTRACTS)['data']),1)
		self.assertGreaterEqual(len(self.deriatives.CommodityDerivatives(self.deriatives.AGRICONTRACTS)['data']),1)
		self.assertGreaterEqual(len(self.deriatives.InterestRateDerivatives(self.deriatives.GOVTSECFUTURES)),1)
	def test_equity_sme_market(self):
		self.assertRaises(ValueError,self.equitySMEMarket.EquityMarketWatch,{})
		self.assertGreaterEqual(len(self.equitySMEMarket.EquityMarketWatch(self.equitySMEMarket.NIFTY_50)),1)
		self.assertGreaterEqual(len(self.equitySMEMarket.SGBMarketWatch()['data']),1)
		self.assertGreaterEqual(len(self.equitySMEMarket.ExchangeTradeFundsWatch()['data']),1)
		self.assertGreaterEqual(len(self.equitySMEMarket.SMEMarketWatch()['data']),1)
	def test_indices(self):
		self.assertGreaterEqual(len(self.indices.IndicesMarketWatch()['data']),1)
	def test_preOpenMarket(self):
		self.assertGreaterEqual(len(self.preOpenMarket.PreOpenMarket(self.preOpenMarket.NIFTYBANK)),1)
		self.assertRaises(ValueError,self.preOpenMarket.PreOpenMarket,{})
if __name__=='__main__':
	unittest.main()