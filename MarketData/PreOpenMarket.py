import requests,logging,json
from MarketData import MarketData
class PreOpenMarket(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._PreOpenMarketBaseURL='https://www.nseindia.com/api/market-data-pre-open'
		self._ValidSymbols=json.load(open('ValidSymbols.json'))['PREOPENMARKET']
	def PreOpenMarket(self,Symbol: str)-> dict:
		return self._GrabData(self._PreOpenMarketBaseURL,{'key': self._ValidSymbols.get(Symbol.upper(),Symbol)})
if __name__=='__main__':
	logging.getLogger('PreOpenMarket').info(PreOpenMarket().PreOpenMarket('NIFTY 50'))