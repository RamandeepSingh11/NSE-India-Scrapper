from ._MarketData import MarketData
from NSE import ValidSymbols
import requests,datetime
class Companies(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self.DateTimeFormat='%d-%m-%Y'
		self._baseURL='https://www.nseindia.com/api/quote-equity'
		self._historicalDataBaseURL='https://www.nseindia.com/api/historical/cm/equity'
		self._validPeriodInputs={'1d': {'days': 1},'1w': {'weeks': 1},'1m': {'days': 30},'3m': {'days' : 90},'6m' : {'days': 180},'1y' : {'days' : 365}}
		for key in ValidSymbols['COMPANIES']:
			setattr(self,key,ValidSymbols['COMPANIES'][key])
	def GetPriceInfo(self,Symbol: str):
		return self._GrabData(self._baseURL,{'symbol': Symbol})
	def GetTradeInfo(self,Symbol: str):
		return self._GrabData(self._baseURL,{'symbol': Symbol,'section': 'trade_info'})
	def _CreateURL(self,Symbol,Series,start: str=None,end: str=None,TimePeriod: str='',Period: bool=True)-> str:
		Series=','.join(Series)
		url=self._historicalDataBaseURL+fr'?symbol={Symbol}&series=[{Series}]'
		if(Period):
			end=datetime.datetime.now()
			start=(end-datetime.timedelta(**self._validPeriodInputs[TimePeriod])).strftime(self.DateTimeFormat)
			end=end.strftime(self.DateTimeFormat)
		url+=rf'&from={start}&to={end}'
		return url
	#Can Take Start and end as either a datetime object or a string.
	def HistoricalData(self,Symbol: str,Series: list[str],TimePeriod: str='',start=None,end=None):
		if(not TimePeriod and (not start or not end)):
			raise Exception('Please Enter a Valid TimePeriod or Starting Date')
		if(start):
			if(type(start)==datetime.datetime):
				start=start.strftime(self.DateTimeFormat)
				end=end.strftime(self.DateTimeFormat)
			elif(type(start)==str):
				try:
					datetime.datetime.strptime(start,self.DateTimeFormat)
					datetime.datetime.strptime(end,self.DateTimeFormat)
				except ValueError:
					raise ValueError(f'Incorrect DateTime Format, Should be {self.DateTimeFormat}')
			else:
				raise Exception('Bad Start and End Value.')
			return self._GrabData(self._CreateURL(Symbol,Series,start=start,end=end,Period=False))
		else:
			if(TimePeriod not in self._validPeriodInputs):
				raise ValueError(f'Incorrect TimePeriod Value, Possible Values are: {list(self._validPeriodInputs.keys())}')
			return self._GrabData(self._CreateURL(Symbol,Series,TimePeriod=TimePeriod))
if __name__=='__main__':
	open('NSE/ValidSymbols.json')