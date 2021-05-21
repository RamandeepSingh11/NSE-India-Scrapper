import json
a=json.load(open('ValidSymbols.json'))['EQUITYDERIVATIVES']
class something:
	def __init__(self):
		for i in a:
			setattr(self,i,a[i])
		print(self.STOCKFUTURES)
print(something().STOCKFUTURES)
(lambda x:(for i in a:print(a[i])))(a)