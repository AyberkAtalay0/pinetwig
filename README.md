# pinetwig 0.2.0
[PineTwig](https://github.com/AyberkAtalay0/pinetwig/) is a pinescript-like financial data analysis and trading package.

## Requirements
- Python 3.7 or above on Windows, Linux or macOS

## Installation
```
pip install pinetwig
```

## Examples
Create ```main.py``` file with one of the following examples:

#### Scraping data from Binance.
```
import pinetwig as pt

df = pt.getDataFromBinance(ticker="BTCUSDT", interval="1h", start="2 day ago UTC", end="now")
print(df)
```

#### Scraping data from TradingView.
```
import pinetwig as pt

df = pt.getDataFromTradingView(symbol="NASDAQ:AAPL", interval="5m", length=5000)
print(df)
```

#### List available indicators.
```
import pinetwig as pt

for i in pt.indicators.all:
    print(i)
```

#### Generating a ray and visualizing.
```
import pinetwig as pt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
ray = pt.ray(x, (0, 0), (2, 1))

pt.visualize(lines={"Values": {"x": x, "y": y}, "Ray": {"x": x, "y": ray}})
```

#### Visualizing a financial dataframe.
```
import pinetwig as pt

df = pt.getDataFromBinance(ticker="BTCUSDT", interval="1h", start="2 day ago UTC", end="now")

df["SMA12"] = pt.sma(df["Close"], 12)

x, y = list(range(len(df))), df["Close"].tolist()
df["Ray1"] = pt.ray(x, (x[0], y[0]), (x[-1], y[-1]*1.02))
df["Ray2"] = pt.ray(x, (x[0], y[0]), (x[-1], y[-1]*0.98))

chart = pt.FancyChart(df, theme="light")
chart.show()
```

## Learn more
- [PineTwig GitHub](https://github.com/AyberkAtalay0/pinetwig/)
- [PineTwig PyPI](https://pypi.org/project/pinetwig/)
