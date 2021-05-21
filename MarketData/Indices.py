from MarketData import MarketData
class Indices(MarketData):
	def __init__(self,timeout: int=5):
		super().__init__(timeout)
		self._BaseURL="https://www.nseindia.com/api/allIndices"
	def IndicesMarketWatch(self):
		return self._GrabData(self._BaseURL)