import requests,logging
from NSE import ValidSymbols
from ._MarketData import MarketData
class PreOpenMarket(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._PreOpenMarketBaseURL='https://www.nseindia.com/api/market-data-pre-open'
		for key in ValidSymbols['PREOPENMARKET']:
			setattr(self,key,ValidSymbols['PREOPENMARKET'][key])
	def PreOpenMarket(self,Symbol: str)-> dict:
		if(type(Symbol)!=str):
			raise ValueError('Invalid Symbol for PreOpenMarket.')
		return self._GrabData(self._PreOpenMarketBaseURL,{'key': Symbol})
if __name__=='__main__':
	# logging.getLogger('PreOpenMarket').info(PreOpenMarket().PreOpenMarket('NIFTY 50'))
	pass