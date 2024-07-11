from .modules import *

# Data

def getDataFromTradingView(ticker, interval, length=5000):
    """
    #### Example Parameters
    - ticker   = "NASDAQ:AAPL"
    - interval = "5m"
    - length   = 5000 (max 5000)
    """

    length = max(length, 5000)

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
    connection.send(stx("quote_add_symbols", [processNo, ticker, {"flags":["force_permission"]}]))
    connection.send(stx("quote_fast_symbols", [processNo, ticker]))
    connection.send(stx("resolve_symbol", [chartNo,"symbol_1", "={\"symbol\":\""+ticker+"\",\"adjustment\":\"splits\",\"session\":\"extended\"}"]))
    connection.send(stx("create_series", [chartNo, "s1", "s1", "symbol_1", interval, length]))

    writed = ""
    while 1:
        try: writed += connection.recv()
        except: break
    out = re.search('"s":\\[(.+?)\\}\\]', writed).group(1)
    x = out.split(',{\"')

    with open(f"{ticker.replace(':', '-')}.csv", mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=0)
        writer.writerow(["Index", "Date", "Open", "High", "Low", "Close", "Volume"])
        for i in x:
            i = re.split("\\[|:|,|\\]", i)
            writer.writerow([int(i[1]), datetime.fromtimestamp(float(i[4])).strftime("%Y-%m-%d %H:%M:%S"), float(i[5]), float(i[6]), float(i[7]), float(i[8]), float(i[9])])    
    
    df = pd.read_csv(f"{ticker.replace(':', '-')}.csv").set_index("Date")
    df["Index"] = list(range(len(df)))
    os.remove(f"{ticker.replace(':', '-')}.csv")
    return df

def getDataFromBinance(ticker, interval, start, end="now"):
    """
    #### Example Parameters
    - ticker   = "BTCUSDT"
    - interval = "5m"
    - start    = "7 day ago UTC"
    - end      = "1 day ago UTC"
    """

    Open = np.array([])
    High = np.array([])
    Low = np.array([])
    Close = np.array([])
    Volume = np.array([])
    Trade = np.array([])
    Index = np.array([])
    Date = np.array([])

    RawData = Client().get_historical_klines(symbol=ticker, interval=interval, start_str=start, end_str=end)
    num = 0
    for candle in RawData:
        Open = np.append(Open, float(candle[1]))
        High = np.append(High, float(candle[2]))
        Low = np.append(Low, float(candle[3]))
        Close = np.append(Close, float(candle[4]))
        Volume = np.append(Volume, float(candle[5]))
        Trade = np.append(Trade, float(candle[8]))
        Date = np.append(Date, datetime.fromtimestamp(int(str(candle[0])[:10])))
        Index = np.append(Index, num)
        num += 1
    return pd.DataFrame.from_dict({"Open": Open, "High": High, "Low": Low, "Close": Close, "Volume": Volume, "Trade": Trade, "Date": Date, "Index": Index}).set_index("Date")