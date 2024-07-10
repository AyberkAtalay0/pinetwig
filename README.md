# pinetwig 0.1.6
[PineTwig](https://pypi.org/project/pinetwig/) is a pinescript-like financial data analysis and trading package.

## Requirements
- Python 3.7 or above on Windows, Linux or macOS

## Installation
```
pip install pinetwig
```

## Examples
Create "main.py" file with one of the following examples:

#### Scraping data from Binance.
```
import pinetwig as pt

data = pt.BinanceData("BTCUSDT", "1h", "2 day ago UTC", "now")
df = data.DataFrame
print(df)
```

#### Scraping data from TradingView.
```
import pinetwig as pt

df = pt.GetTradingViewData(symbol="NASDAQ:AAPL", interval="5m", length=5000)
print(df)
```

#### List available indicators.
```
import pinetwig as pt

for i in pt.indicators.__dir__():
    print(i)
```

## Learn more
- [PineTwig GitHub](https://github.com/AyberkAtalay0/pinetwig/)
- [PineTwig PyPI](https://pypi.org/project/pinetwig/)
