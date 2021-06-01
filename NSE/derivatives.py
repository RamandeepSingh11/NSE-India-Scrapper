import requests,logging
from NSE import ValidSymbols
from ._MarketData import MarketData
class Derivatives(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._EquityDerivatives='https://www.nseindia.com/api/liveEquity-derivatives'
		self._CurrencyDerivatives='https://www.nseindia.com/api/liveCurrency-derivatives'
		self._CommodityDerivatives='https://www.nseindia.com/api/'
		self._InterestRateDerivatives='https://www.nseindia.com/api/liveInterest-rate-future'
		for key in ValidSymbols['DERIVATIVESMARKET']:
			setattr(self,key,ValidSymbols['DERIVATIVESMARKET'][key])
	def EquityDerivatives(self,Symbol: str)->dict:
		if(type(Symbol)==dict):
			raise ValueError('Invalid Symbol for Equity Derivatives.')
		return self._GrabData(self._EquityDerivatives,{'index': Symbol})
	def CurrencyDerivatives(self,Params: dict)->dict:
		if(type(Params)==str):
			raise ValueError('Invalid Symbol for Currency Derivatives.')
		return self._GrabData(self._CurrencyDerivatives,Params)
	def CommodityDerivatives(self,Symbol: str)-> dict:
		if(Symbol=='top20_contracts'):
			return self._GrabData(self._CommodityDerivatives+'commodity-futures')['volume']
		if(type(Symbol)==dict):
			raise ValueError('Invalid Symbol for Commodity Derivatives.')
		return self._GrabData(self._CommodityDerivatives+Symbol)
	def InterestRateDerivatives(self,Params: dict)->dict:
		if(type(Params)==str):
			raise ValueError('Invalid Symbol for Interest Rate Derivatives.')
		return self._GrabData(self._InterestRateDerivatives,Params)
if __name__=='__main__':
	pass