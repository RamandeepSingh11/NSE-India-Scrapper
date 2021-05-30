import importlib.resources,json
with importlib.resources.path('NSE','ValidSymbols.json') as data_path:
	ValidSymbols=json.load(open(data_path))