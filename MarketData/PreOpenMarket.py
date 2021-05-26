import requests,logging,json
from .MarketData import MarketData
class PreOpenMarket(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._PreOpenMarketBaseURL='https://www.nseindia.com/api/market-data-pre-open'
		x=json.load(open('MarketData/ValidSymbols.json'))
		for key in x['PREOPENMARKET']:
			setattr(self,key,x['PREOPENMARKET'][key])
	def PreOpenMarket(self,Symbol: str)-> dict:
		return self._GrabData(self._PreOpenMarketBaseURL,{'key': Symbol})
if __name__=='__main__':
	# logging.getLogger('PreOpenMarket').info(PreOpenMarket().PreOpenMarket('NIFTY 50'))