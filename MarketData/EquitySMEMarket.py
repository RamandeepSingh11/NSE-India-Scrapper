import requests,logging
class EquitySMEMarket:
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._EquityBaseURL='https://www.nseindia.com/api/equity-stockIndices'
		self._SGBBaseURL='https://www.nseindia.com/api/sovereign-gold-bonds'
		self._ExchangeTradeFundsURL="https://www.nseindia.com/api/etf"
		self._SMEMarketBaseURL="https://www.nseindia.com/api/live-analysis-emerge"
	def EquityMarketWatch(self,Indice: str)-> dict:
		Data=self._GrabData(self._EquityBaseURL,{'index' : Indice})
		#Deleting Uncesseary Data.
		Data.pop('metadata')
		Data.pop('date30dAgo')
		Data.pop('date365dAgo')
		return self._RemoveMeta(Data)
	def SGBMarketWatch(self)-> dict:
		return self._RemoveMeta(self._GrabData(self._SGBBaseURL))
	def ExchangeTradeFundsWatch(self)-> dict:
		return self._RemoveMeta(self._GrabData(self._ExchangeTradeFundsURL))
	def SMEMarketWatch(self):
		return self._GrabData(self._SMEMarketBaseURL)
	def _RemoveMeta(self,Data: dict)->dict:
		for i in range(len(Data['data'])):
			if('meta' in Data['data'][i]):
				Data['data'][i].pop('meta')
		return Data
if __name__=='__main__':
	logging.getLogger('EquityMarketWatch').info(EquitySMEMarket().EquityMarketWatch('NIFTY 50'))
	logging.getLogger('SGBMarketWatch').info(EquitySMEMarket().SGBMarketWatch())
	logging.getLogger('ExchangeTradeFundsWatch').info(EquitySMEMarket().ExchangeTradeFundsWatch())
	logging.getLogger('SMEMarket').info(EquitySMEMarket().SMEMarketWatch())