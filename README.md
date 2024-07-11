# pinetwig 0.2.2
[PineTwig](https://pypi.org/project/pinetwig/) is a pinescript-like financial data analysis and trading package.

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

df = pt.getDataFromTradingView(ticker="NASDAQ:AAPL", interval="5m", length=5000)
print(df)
```

#### List available indicators and functions.
```
import pinetwig as pt

print("Indicators:", pt.all_indicators)
print("Functions:", pt.all_functions)
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
df["Linear Reg."] = pt.linreg(list(range(len(df))), df["Close"].tolist())

chart = pt.FancyChart(df, theme="light")
chart.show()
```

## Learn more
- [PineTwig GitHub](https://github.com/AyberkAtalay0/pinetwig/)
- [PineTwig PyPI](https://pypi.org/project/pinetwig/)
