# [NSE-INDIA-API](https://github.com/GamesBond008/NSE-India-API)
#### An Unofficial NSE India API That Scrapes Data From NSE India Without Selenium.
## Installing
Just Clone The Repository and then in the Source Folder do
```bash
pip install -r requirements.txt
```
## Companies 
The Companies Class takes a timeout argument by default it is set to 5 seconds.
```python
from NSE.companies import Companies
Instance=Companies(10)
```
#### Get Price info of a Company
The Method takes Symbol of Company as String
```python
Data=Instance.GetPriceInfo('RBLBANK')
print(Data)
```
Input can Only be String and Symbols of Different Companies can be found on NSEINDIA.
A Example for "RBLBANK" is: 

<a href="https://www.nseindia.com/"><img src="https://imgur.com/SqO844U.png"></a>
<details>
	<summary>Example Result</summary>

```json
{
  "info": {
    "symbol": "RBLBANK",
    "companyName": "RBL Bank Limited",
    "activeSeries": [
      "EQ"
    ],
    "debtSeries": [],
    "tempSuspendedSeries": [],
    "isFNOSec": true,
    "isCASec": false,
    "isSLBSec": true,
    "isDebtSec": false,
    "isSuspended": false,
    "isETFSec": false,
    "isDelisted": false,
    "isin": "INE976G01028",
    "isTop10": false,
    "identifier": "RBLBANKEQN"
  },
  "metadata": {
    "series": "EQ",
    "symbol": "RBLBANK",
    "isin": "INE976G01028",
    "status": "Listed",
    "listingDate": "31-Aug-2016",
    "industry": "PRIVATE SECTOR BANK",
    "lastUpdateTime": "01-Jun-2021 16:00:00",
    "pdSectorPe": 24.28,
    "pdSymbolPe": 25.23,
    "pdSectorInd": "NIFTY BANK                                        "
  },
  "securityInfo": {
    "boardStatus": "Main",
    "tradingStatus": "Active",
    "tradingSegment": "Normal Market",
    "sessionNo": "-",
    "slb": "Yes",
    "classOfShare": "Equity",
    "derivatives": "Yes",
    "surveillance": "-",
    "faceValue": 10,
    "issuedCap": 598020398
  },
  "priceInfo": {
    "lastPrice": 211.5,
    "change": -2.6999999999999886,
    "pChange": -1.2605042016806671,
    "previousClose": 214.2,
    "open": 215.1,
    "close": 211.3,
    "vwap": 212.46,
    "lowerCP": "192.80",
    "upperCP": "235.60",
    "pPriceBand": "No Band",
    "basePrice": 214.2,
    "intraDayHighLow": {
      "min": 210.05,
      "max": 216.3,
      "value": 211.5
    },
    "weekHighLow": {
      "min": 121.3,
      "minDate": "04-Jun-2020",
      "max": 274.3,
      "maxDate": "08-Jan-2021",
      "value": 211.5
    }
  },
  "preOpenMarket": {
    "preopen": [
      {
        "price": 197.45,
        "buyQty": 0,
        "sellQty": 3
      },
      {
        "price": 210,
        "buyQty": 0,
        "sellQty": 17
      },
      {
        "price": 213.2,
        "buyQty": 0,
        "sellQty": 100
      },
      {
        "price": 213.6,
        "buyQty": 0,
        "sellQty": 178
      },
      {
        "price": 215.1,
        "buyQty": 0,
        "sellQty": 0,
        "iep": true
      },
      {
        "price": 218.2,
        "buyQty": 30,
        "sellQty": 0
      },
      {
        "price": 219.35,
        "buyQty": 100,
        "sellQty": 0
      },
      {
        "price": 223,
        "buyQty": 450,
        "sellQty": 0
      },
      {
        "price": 235,
        "buyQty": 75,
        "sellQty": 0
      }
    ],
    "ato": {
      "buy": 2905,
      "sell": 677
    },
    "IEP": 215.1,
    "totalTradedVolume": 6909,
    "finalPrice": 215.1,
    "finalQuantity": 6909,
    "lastUpdateTime": "01-Jun-2021 09:07:19",
    "totalBuyQuantity": 107180,
    "totalSellQuantity": 247785,
    "atoBuyQty": 2905,
    "atoSellQty": 677
  }
}
```
</details>

#### Get Trade Info of a Company

The Method takes Symbol of Company as String
```python
Data=Instance.GetTradeInfo('RBLBANK')
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "noBlockDeals": true,
  "bulkBlockDeals": [
    {
      "name": "Session I"
    },
    {
      "name": "Session II"
    }
  ],
  "marketDeptOrderBook": {
    "totalBuyQuantity": 0,
    "totalSellQuantity": 12414,
    "bid": [
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      }
    ],
    "ask": [
      {
        "price": 211.3,
        "quantity": 12414
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      },
      {
        "price": 0,
        "quantity": 0
      }
    ],
    "tradeInfo": {
      "totalTradedVolume": 6900865,
      "totalTradedValue": 14661.58,
      "totalMarketCap": 1264813.14,
      "ffmc": 829737.0546,
      "impactCost": 0.05
    },
    "valueAtRisk": {
      "securityVar": 24.88,
      "indexVar": 0,
      "varMargin": 24.88,
      "extremeLossMargin": 3.5,
      "adhocMargin": 0,
      "applicableMargin": 28.38
    }
  },
  "securityWiseDP": {
    "quantityTraded": 6900865,
    "deliveryQuantity": 1240171,
    "deliveryToTradedQuantity": 17.97,
    "seriesRemarks": null,
    "secWiseDelPosDate": "01-JUN-2021 EOD"
  }
}
```
</details>

#### Get Historical Data of Company
This Method takes can Take Two Types of Input for Time Periods. Exact Dates or Time Periods(for ex: 1day,1week etc).
##### Example 1
TimePeriod
Input:
1. Symbol of Company in string.
2. Series(List): Possible inputs are Companies().EQ, Companies().RL, Companies().AF
3. Time Period(str): Possible inputs are 1d,1w,1m,3m,6m,1y
```python
Data=Instance.HistoricalData('RBLBANK',[Instance.EQ,Instance.RL],'1d')
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "_id": "60b6217e1746750008d2b0c5",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 216.3,
      "CH_TRADE_LOW_PRICE": 210.05,
      "CH_OPENING_PRICE": 215.1,
      "CH_CLOSING_PRICE": 211.3,
      "CH_LAST_TRADED_PRICE": 211.5,
      "CH_PREVIOUS_CLS_PRICE": 214.2,
      "CH_TOT_TRADED_QTY": 6900865,
      "CH_TOT_TRADED_VAL": 1466218364.55,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 121.3,
      "CH_TOTAL_TRADES": 44144,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-06-01",
      "TIMESTAMP": "2021-05-31T18:30:00.000Z",
      "createdAt": "2021-06-01T12:01:02.542Z",
      "updatedAt": "2021-06-01T12:01:02.542Z",
      "__v": 0,
      "VWAP": 212.47,
      "mTIMESTAMP": "01-Jun-2021"
    },
    {
      "_id": "60b4cffe99942d0008df060a",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 216.4,
      "CH_TRADE_LOW_PRICE": 212.8,
      "CH_OPENING_PRICE": 216.2,
      "CH_CLOSING_PRICE": 214.2,
      "CH_LAST_TRADED_PRICE": 213.8,
      "CH_PREVIOUS_CLS_PRICE": 216.25,
      "CH_TOT_TRADED_QTY": 7126476,
      "CH_TOT_TRADED_VAL": 1529597900.4,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 121.3,
      "CH_TOTAL_TRADES": 39780,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-05-31",
      "TIMESTAMP": "2021-05-30T18:30:00.000Z",
      "createdAt": "2021-05-31T12:01:02.333Z",
      "updatedAt": "2021-05-31T12:01:02.333Z",
      "__v": 0,
      "VWAP": 214.64,
      "mTIMESTAMP": "31-May-2021"
    }
  ],
  "meta": {
    "series": [
      "EQ"
    ],
    "fromDate": "31-05-2021",
    "toDate": "01-06-2021",
    "symbols": [
      "RBLBANK",
      "RBLBANK"
    ]
  }
}
```
</details>

##### Example 2
Start and end Date.
Input:
1. Symbol of Company in string.
2. Series(List): Possible inputs are Companies().EQ, Companies().RL, Companies().AF
3. Start and end(string,datetime.datetime): Date string format should be DD-MM-YYYY
```python
Data=Instance.HistoricalData('RBLBANK',[Instance.EQ,Instance.RL],Start='20-05-2021',End='25-05-2021')
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "_id": "60ace6fd3e1c550008766872",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 211.75,
      "CH_TRADE_LOW_PRICE": 205.05,
      "CH_OPENING_PRICE": 211.5,
      "CH_CLOSING_PRICE": 206.1,
      "CH_LAST_TRADED_PRICE": 206.7,
      "CH_PREVIOUS_CLS_PRICE": 210,
      "CH_TOT_TRADED_QTY": 9106739,
      "CH_TOT_TRADED_VAL": 1891433247.4,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 108.3,
      "CH_TOTAL_TRADES": 50163,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-05-25",
      "TIMESTAMP": "2021-05-24T18:30:00.000Z",
      "createdAt": "2021-05-25T12:01:01.940Z",
      "updatedAt": "2021-05-25T12:01:01.940Z",
      "__v": 0,
      "VWAP": 207.7,
      "mTIMESTAMP": "25-May-2021"
    },
    {
      "_id": "60ab957e03728a0009a357e8",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 212,
      "CH_TRADE_LOW_PRICE": 205.85,
      "CH_OPENING_PRICE": 210,
      "CH_CLOSING_PRICE": 210,
      "CH_LAST_TRADED_PRICE": 209.6,
      "CH_PREVIOUS_CLS_PRICE": 207.7,
      "CH_TOT_TRADED_QTY": 9637361,
      "CH_TOT_TRADED_VAL": 2016371137.35,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 108.3,
      "CH_TOTAL_TRADES": 59436,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-05-24",
      "TIMESTAMP": "2021-05-23T18:30:00.000Z",
      "createdAt": "2021-05-24T12:01:02.566Z",
      "updatedAt": "2021-05-24T12:01:02.566Z",
      "__v": 0,
      "VWAP": 209.22,
      "mTIMESTAMP": "24-May-2021"
    },
    {
      "_id": "60a7a0e0c7277a00086e365a",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 209,
      "CH_TRADE_LOW_PRICE": 205.15,
      "CH_OPENING_PRICE": 207,
      "CH_CLOSING_PRICE": 207.7,
      "CH_LAST_TRADED_PRICE": 207.8,
      "CH_PREVIOUS_CLS_PRICE": 204.25,
      "CH_TOT_TRADED_QTY": 11336046,
      "CH_TOT_TRADED_VAL": 2350319758.8,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 105.5,
      "CH_TOTAL_TRADES": 62694,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-05-21",
      "TIMESTAMP": "2021-05-20T18:30:00.000Z",
      "createdAt": "2021-05-21T12:00:32.096Z",
      "updatedAt": "2021-05-21T12:00:32.096Z",
      "__v": 0,
      "VWAP": 207.33,
      "mTIMESTAMP": "21-May-2021"
    },
    {
      "_id": "60a64f7e9a1015000919d034",
      "CH_SYMBOL": "RBLBANK",
      "CH_SERIES": "EQ",
      "CH_MARKET_TYPE": "N",
      "CH_TRADE_HIGH_PRICE": 207.85,
      "CH_TRADE_LOW_PRICE": 200.35,
      "CH_OPENING_PRICE": 201,
      "CH_CLOSING_PRICE": 204.25,
      "CH_LAST_TRADED_PRICE": 204.95,
      "CH_PREVIOUS_CLS_PRICE": 199.95,
      "CH_TOT_TRADED_QTY": 19971105,
      "CH_TOT_TRADED_VAL": 4081005888,
      "CH_52WEEK_HIGH_PRICE": 274.3,
      "CH_52WEEK_LOW_PRICE": 105.5,
      "CH_TOTAL_TRADES": 88624,
      "CH_ISIN": "INE976G01028",
      "CH_TIMESTAMP": "2021-05-20",
      "TIMESTAMP": "2021-05-19T18:30:00.000Z",
      "createdAt": "2021-05-20T12:01:02.732Z",
      "updatedAt": "2021-05-20T12:01:02.732Z",
      "__v": 0,
      "VWAP": 204.35,
      "mTIMESTAMP": "20-May-2021"
    }
  ],
  "meta": {
    "series": [
      "EQ",
      "RL"
    ],
    "fromDate": "20-05-2021",
    "toDate": "25-05-2021",
    "symbols": [
      "RBLBANK",
      "RBLBANK"
    ]
  }
}
```
</details>

## Derivatives
The Derivatives Class takes a timeout argument by default it is set to 5 seconds.
```python
from NSE.derivatives import Derivatives
Instance=Derivatives(10)
```

#### Equity Derivatives
The EquityDerivatives method takes Symbol argument

Possible Values for Symbol Argument is in format Derivatives().x where x can be:
TOP20CONTRACTS ,STOCKFUTURES ,STOCKOPTIONS ,TOP20SPREADCONTRACTS ,NIFTY50FUTURES ,NIFTY50OPTIONS ,NIFTYBANKFUTURES,
NIFTYBANKOPTIONS ,NIFTYFINANCIALFUTURES ,NIFTYFINANCIALOPTIONS

```python
Data=Instance.EquityDerivatives(Instance.TOP20CONTRACTS)
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "underlying": "BANKNIFTY",
      "identifier": "OPTIDXBANKNIFTY03-06-2021CE35500.00",
      "instrumentType": "OPTIDX",
      "instrument": "Index Options",
      "contract": "BANKNIFTY 03-Jun-2021",
      "expiryDate": "03-Jun-2021",
      "optionType": "Call",
      "strikePrice": 35500,
      "lastPrice": 204.95,
      "change": -162.05,
      "pChange": -44.16,
      "volume": 44008350,
      "totalTurnover": 12002837379,
      "value": 12002837379,
      "premiumTurnOver": 1574299262379,
      "underlyingValue": 35337.2,
      "openInterest": 69778,
      "noOfTrades": 1760334
    },(Truncated)(....)
  ],
  "timestamp": "01-Jun-2021 15:30:00",
  "marketStatus": {
    "market": "FO",
    "marketOpenOrClose": "Open",
    "marketCurrentTradingDate": "Jun 01,2021",
    "marketOpenTime": "0915",
    "marketCloseTime": "1530",
    "marketPreviousTradingDate": "May 31,2021",
    "marketNextTradingDate": "Jun 02,2021",
    "marketStatusMessage": "Market is Closed"
  }
}
```
</details>

#### Currency Derivatives
CurrencyDerivatives method takes Symbol as a argument.

Possible Values for Symbol argument is in format Derivatives().x where x can be:
ALLINRCONTRACTS ,ALLCROSSCURRENCYCONTRACTS ,ALLSPREADCONTRACTS

```python
Data=Instance.CurrencyDerivatives(Instance.ALLINRCONTRACTS)
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "timestamp": "01-Jun-2021 17:00:00",
  "data": [
    {
      "contractType": "USDINR",
      "identifier": "FUTCURUSDINR28-06-2021XX0.0000",
      "instrumentType": "FUTCUR",
      "instrument": "Currency Futures",
      "contract": "USDINR 28-Jun-2021",
      "expiryDate": "28-Jun-2021",
      "optionType": "-",
      "strikePrice": 0,
      "lastPrice": 73.16,
      "change": 0.26500000000000057,
      "pChange": 0.36353659373070935,
      "volume": 2132616,
      "notionalTurnover": 155782901282.5,
      "value": 155782901282.5,
      "openInterest": 2589343,
      "bestBidPrice": 73.16,
      "bestBidQty": 108,
      "bestAskPrice": 73.165,
      "bestAskQty": 56,
      "totTradeVol": 95018,
      "spread": 0.005000000000009663
    },(Truncated)(...)
  ],
  "totalTradedValue": 230753510092.5,
  "totalTradedVolume": 2938297,
  "marketStatus": {
    "market": "Currency",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "",
    "last": "",
    "variation": "",
    "percentChange": "",
    "marketStatusMessage": "Market is Closed"
  }
}
```
</details>

#### Commodity Derivatives
CommodityDerivatives method takes Symbol Argument.

Possible Values for Symbol argument is in format Derivatives().x where x can be:
ALLCOMMODITYCONTRACTS ,AGRICONTRACTS ,BASEMETALCONTRACTS ,BULLIONCONTRACTS ,ENERGYCONTRACTS

```python
Data=Instance.CommodityDerivatives(Instance.ALLCOMMODITYCONTRACTS)
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "identifier": "OPTBLNGOLDM28-06-2021PE47500.0000",
      "instrumentType": "OPTBLN",
      "instrument": "Bullion Options",
      "contract": "GOLDM",
      "unit": "100 Grams",
      "expiryDate": "28-Jun-2021",
      "strikePrice": 47500,
      "optionType": "Put",
      "lastPrice": 165,
      "change": 23.5,
      "pChange": 16.607773851590103,
      "numberOfContractsTraded": 250,
      "totalTurnover": 411260,
      "openInterest": 2,
      "tradeCount": 0,
      "prevClose": 141.5
    },(Truncated)(...)
  ],
  "timestamp": "01-Jun-2021 23:30:00",
  "volume": 844,
  "totalTradedValue": 347047724.764,
  "marketStatus": {
    "market": "Commodity",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "",
    "last": "",
    "variation": "",
    "percentChange": "",
    "marketStatusMessage": "Market is Open"
  }
}
```
</details>

#### Interest Rate Derivatives
InterestRateDerivatives method takes Symbol Argument.

Possible Values for Symbol argument is in format Derivatives().x where x can be:
GOVTSECFUTURES ,GOVTSECOPTS ,TDAY91BILLFUTURES ,OVERNIGHTMIBORFUTURES ,GSECSPREADCONTRACTS

```python
Data=Instance.InterestRateDerivatives(Instance.TDAY91BILLFUTURES)
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "identifier": "FUTIRT91DTB29-09-2021XX0.0000",
      "underlying": "91DTB",
      "underlyingValue": 0,
      "instrumentType": "FUTIRT",
      "instrument": "91 T-Day Bill Futures",
      "contract": "91DTB",
      "strikePrice": 0,
      "optionType": "-",
      "lastPrice": 0,
      "expiryDate": "29-Sep-2021",
      "change": 0,
      "pChange": 0,
      "numberOfContractsTraded": 0,
      "totalTurnover": 0,
      "tradeCount": 0,
      "openInterest": 0,
      "yield": "-"
    },(Truncated)(...)
  ],
  "totalTradedValue": 0,
  "totalTradedVolume": 0,
  "timestamp": "01-Jun-2021 17:00:00",
  "marketStatus": {
    "market": "IRD",
    "marketOpenOrClose": "Open",
    "marketCurrentTradingDate": "Jun 01,2021",
    "marketOpenTime": "0900",
    "marketCloseTime": "1700",
    "marketPreviousTradingDate": "May 31,2021",
    "marketNextTradingDate": "Jun 02,2021",
    "marketStatusMessage": "Market is Closed"
  }
}
```
</details>

## Equity SME Market
EquitySMEMarket Class takes Timeout Argument as input by Default it is 5seconds.
```python
from NSE.equitySMEMarket import EquitySMEMarket
Instance=EquitySMEMarket()
```

#### Equity Market Watch:
EquityMarketWatch Method takes Indice(String) as Argument
Input can Only be String and all Possible Indices Can be found on NSEINDIA.
For Example: 

<img src="https://imgur.com/Wbt0Crl.png">

```python
Data=Instance.EquityMarketWatch("NIFTY FINANCIAL SERVICES 25/50")
print(Data)
```

<details>
	<summary>Example Result</summary>

```json
{
  "name": "NIFTY FINANCIAL SERVICES 25/50",
  "advance": {
    "declines": "17",
    "advances": "3",
    "unchanged": "0"
  },
  "timestamp": "01-Jun-2021 16:00:00",
  "data": [
    {
      "priority": 1,
      "symbol": "NIFTY FINANCIAL SERVICES 25/50",
      "identifier": "NIFTY FINANCIAL SERVICES 25/50",
      "open": 16508.75,
      "dayHigh": 16576.55,
      "dayLow": 16346.7,
      "lastPrice": 16417.5,
      "previousClose": 16450.25,
      "change": -32.75,
      "pChange": -0.2,
      "ffmc": 253618480.76,
      "yearHigh": 0,
      "yearLow": 0,
      "totalTradedVolume": 123443084,
      "totalTradedValue": 96694971930.81,
      "lastUpdateTime": "01-Jun-2021 16:00:00",
      "nearWKH": null,
      "nearWKL": null,
      "perChange365d": "-",
      "date365dAgo": "-",
      "chart365dPath": "-",
      "date30dAgo": "30-Apr-2021",
      "perChange30d": 6.79,
      "chart30dPath": "https://static.nseindia.com/sparklines/30d/NIFTY-FINSRV25-50.jpg",
      "chartTodayPath": "https://static.nseindia.com/sparklines/today/NIFTY-FINSRV25-50.jpg"
    },(Truncated)(...)
  ],
  "marketStatus": {
    "market": "Capital Market",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "NIFTY 50",
    "last": 15574.85,
    "variation": -7.949999999998909,
    "percentChange": -0.05,
    "marketStatusMessage": "Normal Market has Closed"
  }
}
```
</details>

#### SGB Market Watch

```python
Data=Instance.SGBMarketWatch()
print(Data)
```

<details>
	<summary>Example Result</summary>

```json
{
  "timestamp": "01-Jun-2021 16:00:00",
  "data": [
    {
      "symbol": "SGBNOV25",
      "open": "4920",
      "high": "4939.99",
      "low": "4920",
      "issue_price": "2884",
      "ltP": "4920",
      "chn": "163.99",
      "per": "3.45",
      "qty": "8",
      "trdVal": "39439.92",
      "wkhi": "5399",
      "wklo": "4521",
      "xDt": null,
      "cAct": null,
      "yPC": 7.760036796110129,
      "mPC": 0.9234909681680836,
      "prevClose": "4756.01",
      "nearWKH": 8.872013335802926,
      "nearWKL": -8.825481088254811,
      "maturityDate": "NOV25",
      "chartTodayPath": "https://static.nseindia.com/sparklines/today/SGBNOV25GBN.jpg",
      "perChange365d": 3.82,
      "date365dAgo": "29-May-2020",
      "chart365dPath": "https://static.nseindia.com/sparklines/365d/SGBNOV25-GB.jpg",
      "date30dAgo": "30-Apr-2021",
      "perChange30d": 1.13,
      "chart30dPath": "https://static.nseindia.com/sparklines/30d/SGBNOV25-GB.jpg"
    },(Truncated)(...)
  ],
  "advances": 28,
  "declines": 11,
  "unchanged": 10,
  "totalTradedValue": 23821747.18,
  "totalTradedVolume": 4926,
  "totalPercentChange": 9.04,
  "marketStatus": {
    "market": "Capital Market",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "NIFTY 50",
    "last": 15574.85,
    "variation": -7.949999999998909,
    "percentChange": -0.05,
    "marketStatusMessage": "Normal Market has Closed"
  }
}
```
</details>

#### Exchange Trade Funds Watch

```python
Data=Instance.ExchangeTradeFundsWatch()
print(Data)
```

<details>
	<summary>Example Result</summary>

```json
{
  "timestamp": "01-Jun-2021 16:00:00",
  "data": [
    {
      "symbol": "IBMFNIFTY",
      "assets": "Nifty 50",
      "open": "152.6",
      "high": "155",
      "low": "150.52",
      "ltP": "155",
      "chn": "4.28",
      "per": "2.84",
      "qty": "3949",
      "trdVal": "600642.9",
      "nav": "160.6795",
      "wkhi": "174",
      "wklo": "101.5",
      "xDt": "-",
      "cAct": "-",
      "yPC": 44.85981308411215,
      "mPC": 3.7136165941786627,
      "prevClose": "150.72",
      "nearWKH": 10.919540229885058,
      "nearWKL": -52.70935960591133,
      "chartTodayPath": "https://static.nseindia.com/sparklines/today/IBMFNIFTYEQN.jpg",
      "perChange365d": 43.49,
      "date365dAgo": "29-May-2020",
      "chart365dPath": "https://static.nseindia.com/sparklines/365d/IBMFNIFTY-EQ.jpg",
      "date30dAgo": "30-Apr-2021",
      "perChange30d": 1.84,
      "chart30dPath": "https://static.nseindia.com/sparklines/30d/IBMFNIFTY-EQ.jpg"
    },(Truncated)(...)
  ],
  "advances": 54,
  "declines": 29,
  "unchanged": 5,
  "navDate": "31-May-2021",
  "totalTradedValue": 2726620745.37,
  "totalTradedVolume": 20700494,
  "marketStatus": {
    "market": "Capital Market",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "NIFTY 50",
    "last": 15574.85,
    "variation": -7.949999999998909,
    "percentChange": -0.05,
    "marketStatusMessage": "Normal Market has Closed"
  }
}
```
</details>

#### SME Market Watch

```python
Data=Instance.SMEMarketWatch()
print(Data)
```

<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "symbol": "LAXMICOT",
      "series": "SM",
      "open": 15.7,
      "dayHigh": 15.8,
      "dayLow": 15.5,
      "lastPrice": 15.8,
      "change": 1.5500000000000007,
      "pChange": 10.877192982456146,
      "previousClose": 14.25,
      "totalTradedVolume": 18000,
      "totalTradedValue": 281880,
      "yearHigh": 17.7,
      "yearLow": 7.5,
      "nearWKH": 10.73446327683615,
      "nearWKL": -110.66666666666669,
      "ca": " ",
      "chartTodayPath": "https://static.nseindia.com/sparklines/today/LAXMICOTSMN.jpg",
      "perChange365d": 86.27,
      "date365dAgo": "29-May-2020",
      "chart365dPath": "https://static.nseindia.com/sparklines/365d/LAXMICOT-SM.jpg",
      "date30dAgo": "29-Apr-2021",
      "perChange30d": 23.91,
      "chart30dPath": "https://static.nseindia.com/sparklines/30d/LAXMICOT-SM.jpg"
    },(Truncated)(...)
  ],
  "timestamp": "01-Jun-2021 16:00:00",
  "adv": 28,
  "dec": 35,
  "noChg": 5,
  "totalTradedValue": 46922702.69,
  "totalTradedVolume": 993197,
  "marketStatus": {
    "market": "Capital Market",
    "marketStatus": "Closed",
    "tradeDate": "02-Jun-2021",
    "index": "NIFTY 50",
    "last": 15574.85,
    "variation": -7.949999999998909,
    "percentChange": -0.05,
    "marketStatusMessage": "Normal Market has Closed"
  }
}
```
</details>

## Indices Market Watch
Indices Class Takes timeout argument by Default it is set to 5seconds.

```python
from NSE.indices import Indices
Instance=Indices()
```

#### Indices Market Watch
```python
Data=Instance.IndicesMarketWatch()
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "data": [
    {
      "key": "BROAD MARKET INDICES",
      "index": "NIFTY 50",
      "indexSymbol": "NIFTY 50",
      "last": 15574.85,
      "variation": -7.95,
      "percentChange": -0.05,
      "open": 15629.65,
      "high": 15660.75,
      "low": 15528.3,
      "previousClose": 15582.8,
      "yearHigh": 15660.75,
      "yearLow": 9544.35,
      "pe": "28.87",
      "pb": "4.39",
      "dy": "1.07",
      "declines": "31",
      "advances": "19",
      "unchanged": "0",
      "perChange365d": 62.65,
      "date365dAgo": "29-May-2020",
      "chart365dPath": "https://static.nseindia.com/sparklines/365d/NIFTY-50.jpg",
      "date30dAgo": "30-Apr-2021",
      "perChange30d": 6.5,
      "chart30dPath": "https://static.nseindia.com/sparklines/30d/NIFTY-50.jpg",
      "chartTodayPath": "https://static.nseindia.com/sparklines/today/NIFTY-50.jpg",
      "previousDay": 15435.65,
      "oneWeekAgo": 15208.45,
      "oneMonthAgo": 14631.1,
      "oneYearAgo": 9580.3
    },(Truncated)(...)
  ],
  "timestamp": "01-Jun-2021 15:30:00",
  "advances": 884,
  "declines": 1909,
  "unchanged": 25,
  "dates": {
    "previousDay": "28-May-2021",
    "oneWeekAgo": "25-May-2021",
    "oneMonthAgo": "30-Apr-2021",
    "oneYearAgo": "29-May-2020"
  },
  "date30dAgo": "30-Apr-2021",
  "date365dAgo": "29-May-2020"
}
```
</details>

## Pre Open Market Watch
PreOpenMarket Takes timeout as argument by default it is set to 5seconds

```python
from NSE.preOpenMarket import PreOpenMarket
Instance=PreOpenMarket(10)
```

#### Pre Open Market
PreOpenMarket Method takes Symbol as argument in format PreOpenMarket().x where x is:
NIFTYBANK ,NIFTY50 ,EMERGE ,SECURITIESINFO
```python
Data=Instance.PreOpenMarket(Instance.SECURITIESINFO)
print(Data)
```
<details>
	<summary>Example Result</summary>

```json
{
  "declines": 11,
  "unchanged": 6,
  "data": [
    {
      "metadata": {
        "symbol": "BEL",
        "identifier": "BELEQN",
        "purpose": " INTERIM DIVIDEND - RS 1.40  PER SHARE",
        "lastPrice": 153,
        "change": 7.599999999999994,
        "pChange": 5.2269601100412615,
        "previousClose": 145.4,
        "finalQuantity": 323384,
        "totalTurnover": 49477752,
        "marketCap": 173597500816.98,
        "yearHigh": 160,
        "yearLow": 67.4,
        "iep": 153,
        "chartTodayPath": "https://static.nseindia.com/sparklines/today/preOpen_BELEQN.jpg"
      },
      "detail": {
        "preOpenMarket": {
          "preopen": [
            {
              "price": 138.15,
              "buyQty": 0,
              "sellQty": 3439
            },
            {
              "price": 144,
              "buyQty": 0,
              "sellQty": 200
            },
            {
              "price": 144.9,
              "buyQty": 0,
              "sellQty": 24
            },
            {
              "price": 145,
              "buyQty": 0,
              "sellQty": 3209
            },
            {
              "price": 153,
              "buyQty": 0,
              "sellQty": 0,
              "iep": true
            },
            {
              "price": 156.95,
              "buyQty": 37088,
              "sellQty": 0
            },
            {
              "price": 158,
              "buyQty": 100,
              "sellQty": 0
            },
            {
              "price": 158.1,
              "buyQty": 50,
              "sellQty": 0
            },
            {
              "price": 159,
              "buyQty": 250,
              "sellQty": 0
            }
          ],
          "ato": {
            "totalBuyQuantity": 249734,
            "totalSellQuantity": 6945
          },
          "IEP": 153,
          "totalTradedVolume": 323384,
          "finalPrice": 153,
          "finalQuantity": 323384,
          "lastUpdateTime": "01-Jun-2021 09:07:22",
          "totalSellQuantity": 510557,
          "totalBuyQuantity": 686414,
          "atoBuyQty": 249734,
          "atoSellQty": 6945
        }
      }
    },(Truncated)(...)
  ],
  "advances": 139,
  "timestamp": "01-Jun-2021 09:07:24",
  "totalTradedValue": 11994.124397500002,
  "totalmarketcap": 847507154.7767485,
  "totalTradedVolume": 3455859
}
```
</details>
