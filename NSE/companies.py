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
	def _CreateURL(self,Symbol,Series,Start: str=None,End: str=None,TimePeriod: str='',Period: bool=True)-> str:
		Series=','.join(Series)
		url=self._historicalDataBaseURL+fr'?symbol={Symbol}&series=[{Series}]'
		if(Period):
			End=datetime.datetime.now()
			Start=(End-datetime.timedelta(**self._validPeriodInputs[TimePeriod])).strftime(self.DateTimeFormat)
			End=End.strftime(self.DateTimeFormat)
		url+=rf'&from={Start}&to={End}'
		return url
	#Can Take Start and End as either a datetime object or a string.
	def HistoricalData(self,Symbol: str,Series: list[str],TimePeriod: str='',Start=None,End=None):
		if(type(Series)!=list):
			raise ValueError('Please Enter a List type for Series.')
		if(not TimePeriod and (not Start or not End) or (type(TimePeriod)!=str )):
			raise ValueError('Please Enter a Valid TimePeriod or Starting Date')
		if(Start):
			if(type(Start)==datetime.datetime and type(End)==datetime.datetime):
				Start=Start.strftime(self.DateTimeFormat)
				End=End.strftime(self.DateTimeFormat)
			elif(type(Start)==str and type(End)==str):
				try:
					datetime.datetime.strptime(Start,self.DateTimeFormat)
					datetime.datetime.strptime(End,self.DateTimeFormat)
				except ValueError:
					raise ValueError(f'Incorrect DateTime Value/Format,\n Accepted Values are Str and Datetime object\n Format for string Should be {self.DateTimeFormat}')
			else:
				raise Exception('Bad Start or End Value.')
			res=self._GrabData(self._CreateURL(Symbol,Series,Start=Start,End=End,Period=False))
		else:
			if(TimePeriod not in self._validPeriodInputs):
				raise ValueError(f'Incorrect TimePeriod Value, Possible Values are: {list(self._validPeriodInputs.keys())}')
			res=self._GrabData(self._CreateURL(Symbol,Series,TimePeriod=TimePeriod))
		if(res.get('error')):
			raise Exception(res['showMessage'])
		return res
if __name__=='__main__':
	open('NSE/ValidSymbols.json')