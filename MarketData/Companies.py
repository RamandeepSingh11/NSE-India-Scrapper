from .MarketData import MarketData
import requests
class Companies(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout	)
		self._baseURL='https://www.nseindia.com/api/quote-equity'
	def GetPriceInfo(self,Symbol: str):
		return self._GrabData(self._baseURL,{'symbol': Symbol})
	def GetTradeInfo(self,Symbol: str):
		return self._GrabData(self._baseURL,{'symbol': Symbol,'section': 'trade_info'})