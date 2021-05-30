import requests,logging
# logging.basicConfig(filename='output.log',level=logging.INFO)
class MarketData:
	def __init__(self,timeout):
		self.session=requests.Session()
		self._timeout=timeout
		self.session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
		self.session.get('https://www.nseindia.com/market-data/live-equity-market',timeout=self._timeout)
	def _GrabData(self,BaseUrl: str,params: dict={})-> dict:
		try:
			response=self.session.get(BaseUrl,params=params,timeout=self._timeout)
			if(response.status_code!=200 or response.text.find('Resource not found')!=-1):
				self.__init__(self._timeout)
				response=self.session.get(BaseUrl,params=params,timeout=self._timeout)
				if(response.status_code!=200 or response.text.find('Resource not found')!=-1):
					raise RuntimeError("Couldn't Connect to the NSEIndia. Please Try Again.\n It Could Be cause of the Bad input Parameters or Bad URL.")
			return response.json()
		except requests.exceptions.RequestException as e:
			raise SystemExit(e)