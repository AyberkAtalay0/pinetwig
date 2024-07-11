from .modules import *
from .functions import *

# Visualization

def visualize(lines, filename=None):
    """
    #### Example Parameters
    - lines    = {"line1": {"x": [0, 1, 2, 3, 4], "y": [-1, 0, -2, 0, 1]}, "line2": ...}
    - filename = None
    """

    if not type(lines) == dict: raise Exception("visualize(): 'lines' is not a dictionary.")

    elems = []
    for axs in lines.values():
        x, y = axs["x"], axs["y"]
        if not type(x) in (list, tuple, np.ndarray): raise Exception("visualize(): 'x' is not an array.")
        if not type(y) in (list, tuple, np.ndarray): raise Exception("visualize(): 'y' is not an array.")
        if not len(x) == len(y): raise Exception("visualize(): 'x' and 'y' must be the same length.")
        elems.append(plt.plot(x, y))
    plt.legend(elems, list(lines.keys()))

    if filename == None:
        plt.show()
    else:
        if not filename.endswith(".png"): filename += ".png"
        plt.savefig(filename)

class FancyChart():
    def __init__(self, df: pd.DataFrame, title="", theme="light", text_color=None, grid_color=None, toolbar=True, xslider=False):
        self.BlockingLines = ("Open", "Close", "High", "Low", "Volume", "Trade", "Index", "Date")
        self.Rows = highest([int(str(col).upper().split("ROW")[1][0]) if "ROW" in str(col).upper() else 1 for col in df.columns])[0]
        self.Cols = highest([int(str(col).upper().split("COL")[1][0]) if "COL" in str(col).upper() else 1 for col in df.columns])[0]
        self.PaperColor = "rgba(250,250,250,255)"
        self.PlotColor = "rgba(250,250,250,255)"
        self.GridColor = "rgba(220,220,220,255)" if grid_color == None else grid_color
        self.Toolbar = toolbar
        self.XSlider = xslider
        self.Theme = theme
        self.Title = title
        self.DataFrame = df
        self.TextColor = text_color
        TextColor = "rgba(155,155,155,255)"
        SpikeColor = "#000000"
        if "Date" in self.DataFrame.columns: self.DataFrame.set_index("Date")
        if "transp" in theme: self.PaperColor, self.PlotColor, self.GridColor, TextColor = "rgba(0,0,0,0)", "rgba(0,0,0,0)", "rgba(0,0,0,0)", "#000000"
        elif "dark" in theme: self.PaperColor, self.PlotColor, self.GridColor, TextColor, SpikeColor = "#131722", "#131722", "#242733", "#B2B5BE", "#9598A1"
        if self.TextColor != None: TextColor = self.TextColor
        def clearname(text): return str(text).upper().replace("ROW1","").replace("ROW2","").replace("ROW3","").replace("ROW4","").replace("ROW5","").replace("COL1","").replace("COL2","").replace("COL3","").replace("COL4","").replace("COL5","").replace("MARKER","").strip().capitalize()
        fig = make_subplots(rows=self.Rows, cols=self.Cols, shared_xaxes=True)
        try: fig.add_trace(go.Candlestick(x=self.DataFrame.index, open=self.DataFrame["Open"], high=self.DataFrame["High"], low=self.DataFrame["Low"], close=self.DataFrame["Close"], increasing_line_color="#1EC1DB", decreasing_line_color= "#F30845", name="Candles"), row=1, col=1)
        except: pass
        for col in self.DataFrame.columns:
            if (not "invisible" in str(col).lower()) and (not str(col).capitalize() in self.BlockingLines):
                mode = "lines"
                if "MARKER" in str(col).upper(): mode = "markers" 
                r = int(str(col).upper().split("ROW")[1][0]) if "ROW" in str(col).upper() else 1
                c = int(str(col).upper().split("COL")[1][0]) if "COL" in str(col).upper() else 1
                fig.add_trace(go.Scatter(x=self.DataFrame.index, y=self.DataFrame[str(col)], mode=mode, name=clearname(col)), row=r, col=c)
        fig.update_layout(modebar_add=["drawline", "drawopenpath", "drawcircle", "drawrect", "eraseshape"], xaxis_visible=True, xaxis_rangeslider_visible=self.XSlider, legend_title=self.Title, font=dict(family="Courier New, monospace", size=18, color=TextColor), paper_bgcolor=self.PaperColor, plot_bgcolor=self.PlotColor)
        fig.update_yaxes(gridcolor=self.GridColor, showgrid=True, title_text="Value", showspikes=True, spikethickness=1, spikecolor=SpikeColor, spikemode="toaxis+across")
        fig.update_xaxes(gridcolor=self.GridColor, showgrid=True, title_text=str(self.DataFrame.index.name), showspikes=True, spikethickness=1, spikecolor=SpikeColor, spikemode="toaxis+across")
        fig.update_traces(xaxis="x1")
        self.Figure = fig

    def show(self, toolbar=True, logo=False, scrollZoom=False, fromFile=True): 
        if fromFile: 
            hexID = random.randint(1000000000000000, 9999999999999999)
            self.save(fname=f"figure-{hexID}.html")
            os.system(f"figure-{hexID}.html")
        else: self.Figure.show(config={"displayModeBar": toolbar, "displaylogo": logo, "scrollZoom": scrollZoom})

    def save(self, fname="figure.html"): 
        with open(f"{fname}", "w") as graph:
            text = self.Figure.to_html(full_html=True, include_plotlyjs="cdn").replace("<body>", f'<body style="background-color: {self.PaperColor}">')
            graph.write(text)

    def getHTML(self): return self.Figure.to_html(full_html=True, include_plotlyjs="cdn").replace("<body>", f'<body style="background-color: {self.PaperColor}">')