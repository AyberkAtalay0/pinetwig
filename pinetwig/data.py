from .modules import *

#Data
def GetTradingViewData(symbol, interval, length=5000):
    """
    Example Parameters;
    symbol = "NASDAQ:AAPL"
    interval = "5m"
    length = 5000 (max 5000)
    """
    keys = list("abcdefghijklmnoprstuvyzwx")
    chars = ["\\","`","*","_","{","}","[","]","(",")",">","#","+","-",".","!","$","\""]+keys
    for i in chars: interval = interval.replace(i, "")
    def stx(func, paramList):
        text = json.dumps({"m":func, "p":paramList}, separators=(",", ":"))
        return "~m~" + str(len(text)) + "~m~" + text
    connection = create_connection("wss://data.tradingview.com/socket.io/websocket", headers=json.dumps({"Origin": "https://data.tradingview.com"}))
    processNo = "qs_" +"".join(random.choice(keys) for i in range(12))
    chartNo = "cs_" +"".join(random.choice(keys) for i in range(12))
    connection.send(stx("set_auth_token", ["unauthorized_user_token"]))
    connection.send(stx("chart_create_session", [chartNo, ""]))
    connection.send(stx("quote_create_session", [processNo]))
    connection.send(stx("quote_set_fields", [processNo, "ch", "chp", "current_session", "description", "local_description", "language", "exchange", "fractional", "is_tradable", "lp", "lp_time", "minmov", "minmove2", "original_name", "pricescale", "pro_name", "short_name", "type", "update_mode", "volume", "currency_code", "rchp", "rtc"]))
    connection.send(stx("quote_add_symbols", [processNo, symbol, {"flags":["force_permission"]}]))
    connection.send(stx("quote_fast_symbols", [processNo, symbol]))
    connection.send(stx("resolve_symbol", [chartNo,"symbol_1", "={\"symbol\":\""+symbol+"\",\"adjustment\":\"splits\",\"session\":\"extended\"}"]))
    connection.send(stx("create_series", [chartNo, "s1", "s1", "symbol_1", interval, length]))
    writed = ""
    while 1:
        try: writed += connection.recv()
        except: break
    out = re.search('"s":\\[(.+?)\\}\\]', writed).group(1)
    x = out.split(',{\"')
    with open(f"{symbol.replace(':', '-')}.csv", mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=0)
        writer.writerow(["Index", "Date", "Open", "High", "Low", "Close", "Volume"])
        for i in x:
            i = re.split("\\[|:|,|\\]", i)
            writer.writerow([int(i[1]), datetime.fromtimestamp(float(i[4])).strftime("%Y-%m-%d %H:%M:%S"), float(i[5]), float(i[6]), float(i[7]), float(i[8]), float(i[9])])    
    df = pd.read_csv(f"{symbol.replace(':', '-')}.csv").set_index("Date")
    remove(f"{symbol.replace(':', '-')}.csv")
    return df

class BinanceData():
    def __init__(self, ticker, interval, start, end):
        """
        Example Parameters;
        ticker   = "BTCUSDT",
        interval = "5m",
        start    = "7 day ago UTC",
        end      = "1 day ago UTC"
        """

        self.Ticker = ticker
        self.Interval = interval
        self.Start = start
        self.End = end

        self.Open = np.array([])
        self.High = np.array([])
        self.Low = np.array([])
        self.Close = np.array([])
        self.Volume = np.array([])
        self.Trade = np.array([])
        self.Index = np.array([])
        self.Date = np.array([])
        self.DataFrame = pd.DataFrame.from_dict({"Open": self.Open, "High": self.High, "Low": self.Low, "Close": self.Close, "Volume": self.Volume, "Trade": self.Trade, "Date": self.Date, "Index": self.Index}).set_index("Date")

        self.Client = Client()
        self.load()
        
    def load(self):
        self.RawData = self.Client.get_historical_klines(symbol=self.Ticker, interval=self.Interval, start_str=self.Start, end_str=self.End)
        num = 0
        for candle in self.RawData:
            self.Open = np.append(self.Open, float(candle[1]))
            self.High = np.append(self.High, float(candle[2]))
            self.Low = np.append(self.Low, float(candle[3]))
            self.Close = np.append(self.Close, float(candle[4]))
            self.Volume = np.append(self.Volume, float(candle[5]))
            self.Trade = np.append(self.Trade, float(candle[8]))
            self.Date = np.append(self.Date, datetime.fromtimestamp(int(str(candle[0])[:10])))
            self.Index = np.append(self.Index, num)
            num += 1
        self.DataFrame = pd.DataFrame.from_dict({"Open": self.Open, "High": self.High, "Low": self.Low, "Close": self.Close, "Volume": self.Volume, "Trade": self.Trade, "Date": self.Date, "Index": self.Index}).set_index("Date")

    def reload(self):
        self.load()
