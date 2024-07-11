"""
A pinescript-like financial data analysis and trading package
"""

__title__ = "pinetwig"
__description__ = "A pinescript-like financial data analysis and trading package"
__url__ = "https://pypi.org/project/pinetwig/"
__version__ = "0.2.2"
__author__ = "Ayberk ATALAY"
__author_email__ = "ayberkatalaypersonal@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2024 Ayberk ATALAY"

from .functions import all_functions, cos, sin, tan, exp, pow, abst, sqrt, floor, ceil, factorial, multlist, divlist, addlist, substlist, sum, change, changeper, roc, avg, covariance, variance, max, min, highest, lowest, nz, stdev, ray, linreg
from .indicators import all_indicators, tr, atr, sma, ema, rma, wma, hma, rsi, vwma
from .data import getDataFromTradingView, getDataFromBinance
from .visualization import visualize, FancyChart