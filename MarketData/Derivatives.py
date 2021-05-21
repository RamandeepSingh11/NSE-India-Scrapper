import requests,logging,json
from MarketData import MarketData
class Derivatives(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._EquityDerivatives='https://www.nseindia.com/api/liveEquity-derivatives'
		self._CurrencyDerivatives='https://www.nseindia.com/api/liveCurrency-derivatives'
		self._CommodityDerivatives='https://www.nseindia.com/api/'
		self._InterestRateDerivatives='https://www.nseindia.com/api/liveInterest-rate-future'
		x=json.load(open('ValidSymbols.json'))
		for key in x['DERIVATIVESMARKET']:
			setattr(self,key,x['DERIVATIVESMARKET'][key])
	def EquityDerivatives(self,Symbol: str)->dict:
		return self._GrabData(self._EquityDerivatives,{'index': self._ValidSymbols.get(Symbol.upper(),Symbol)})
	def CurrencyDerivatives(self,Params: dict)->dict:
		return self._GrabData(self._CurrencyDerivatives,Params)
	def CommodityDerivatives(self,Symbol: str)-> dict:
		if(params=='top20_contracts'):
			return self._GrabData(self._CommodityDerivatives+'commodity-futures')['volume']
		return self._GrabData(self._CommodityDerivatives+params)
	def InterestRateDerivaties(self,Params: dict)->dict:
		return self._GrabData(self._InterestRateDerivatives,Params)
if __name__=='__main__':
	logging.getLogger('EquityDerivatives').info(Derivatives().EquityDerivatives('top 20 contracts'))