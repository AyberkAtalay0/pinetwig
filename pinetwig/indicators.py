from .modules import *
from .functions import *

# Decorator
all = []
def register():
    def wrapper(f):
        all.append(f.__name__)
        return f
    return wrapper

# Indicators

@register()
def tr(close, high, low, type=1):
    cl, hi, lo = [i for i in close], [i for i in high], [i for i in low]
    srdf = pd.DataFrame({"cl":cl, "hi":hi, "lo":lo})
    high_low = srdf["hi"] - srdf["lo"]
    high_close = np.abs(srdf["hi"] - srdf["cl"].shift())
    low_close = np.abs(srdf["lo"] - srdf["cl"].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    x1 = np.max(ranges, axis=1)
    return x1.tolist() if type==1 else x1

@register()
def atr(close, high, low, period, type=1):
    cl, hi, lo = [i for i in close], [i for i in high], [i for i in low]
    srdf = pd.DataFrame({"tr":tr(close, high, low)})
    x1 = srdf["tr"].rolling(period).sum()/period
    return x1.tolist() if type==1 else x1

@register()
def sma(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    x1 = srdf["src"].rolling(period).mean()
    return x1.tolist() if type==1 else x1

@register()
def ema(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    x1 = srdf["src"].ewm(span=period, adjust=False).mean()
    return x1.tolist() if type==1 else x1

@register()
def rma(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    x1, ma = [], sma(src, period)
    for i in range(len(src)):
        if i <= period+2: x1.append(ma[i])
        else: x1.append((src[i]+(period-1)*x1[-1])/period)
    return x1 if type==1 else pd.DataFrame({"x":x1})["x"]

@register()
def wma(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    x1 = srdf["src"].rolling(period).apply(lambda x: ((np.arange(period)+1)*x).sum()/(np.arange(period)+1).sum(), raw=True)
    return x1.tolist() if type==1 else x1

@register()
def hma(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    x1 = wma(wma(source, period//2, type=2).multiply(2).sub(wma(source, period)), int(sqrt(period)), type=2)
    return x1.tolist() if type==1 else x1

@register()
def rsi(source, period, type=1):
    src = [i for i in source]
    srdf = pd.DataFrame({"src":src})
    delta = srdf["src"].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = sma(up, period, type=2)
    ma_down = sma(down, period, type=2)
    x1 = 100 - (100 / (1 + ma_up / ma_down))
    return x1.tolist() if type==1 else x1

@register()
def vwma(source, volume, period, type=1):
    src, vol = [i for i in source], [i for i in volume]
    mldf = pd.DataFrame({"mlt":multlist(src, vol)})
    x1 = divlist(sma(mldf["mlt"], period), sma(vol, period))
    return x1 if type==1 else pd.DataFrame({"x":x1})["x"]