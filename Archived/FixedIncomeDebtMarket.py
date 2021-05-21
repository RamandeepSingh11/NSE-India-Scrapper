import requests
from MarketData import MarketData
class FixedIncomeDebtMarket(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._TradedOnCM="https://www.nseindia.com/api/liveBonds-traded-on-cm"
		self._CorporateBonds="https://www.nseindia.com/api/liveCorp-bonds"
	def TradedOnCM(self,params: dict)->dict:
		return self._RemoveMeta(self._GrabData(self._TradedOnCM,params))
	def CorporateBonds(self,params: dict)-> dict:
		response=self._GrabData(self._CorporateBonds,params)
		response.pop('descriptors')
		return response
	def _RemoveMeta(self,res: dict)->dict:
		for x in range(len(res['data'])):
			res['data'][x].pop('meta')
		return res