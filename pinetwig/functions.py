import math, pandas as pd, numpy as np

# Decorator

all_functions = []
def register_function():
    def wrapper(f):
        all_functions.append(f.__name__)
        return f
    return wrapper

# Math Functions

@register_function()
def cos(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("cos(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.cos(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("cos(): Element is not a float or integer.")
            output.append(math.cos(i))
        return output

@register_function()
def sin(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("sin(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.sin(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("sin(): Element is not a float or integer.")
            output.append(math.sin(i))
        return output

@register_function()
def tan(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("tan(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.tan(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("tan(): Element is not a float or integer.")
            output.append(math.tan(i))
        return output

@register_function()
def exp(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("exp(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.exp(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("exp(): Element is not a float or integer.")
            output.append(math.exp(i))
        return output

@register_function()
def pow(var1, var2): 
    if (not type(var1) in (list, tuple, np.ndarray, int, float)) and (not type(var2) in (int, float)): raise Exception("pow(): Variable is not an array, float or integer.")
    if type(var1) in (int, float): 
        return var1**var2
    else:
        output = []
        for i in var1:
            if not type(i) in (int, float): raise Exception("pow(): Element is not a float or integer.")
            output.append(i**var2)
        return output

@register_function()
def abst(var):
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("abst(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return abs(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("abst(): Element is not a float or integer.")
            output.append(abs(i))
        return output

@register_function()
def sqrt(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("sqrt(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.sqrt(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("sqrt(): Element is not a float or integer.")
            output.append(math.sqrt(i))
        return output

@register_function()
def floor(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("floor(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.floor(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("floor(): Element is not a float or integer.")
            output.append(math.floor(i))
        return output

@register_function()
def ceil(var): 
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("ceil(): Variable is not an array, float or integer.")
    if type(var) in (int, float): 
        return math.ceil(var)
    else:
        output = []
        for i in var:
            if not type(i) in (int, float): raise Exception("ceil(): Element is not a float or integer.")
            output.append(math.ceil(i))
        return output

@register_function()
def factorial(var):
    if not type(var) in (list, tuple, np.ndarray, int, float): raise Exception("factorial(): Variable is not an array, float or integer.")
    if type(var) == int:
        result = 1
        for i in range(0, var-1): result *= var-i
    elif type(var) in (list, tuple, np.ndarray): 
        result = []
        for e in var:
            if type(e) != int and type(e) != float: raise Exception("factorial(): Element is not a float or integer.")
            result.append(1)
            for i in range(0, e-1): result[-1] *= e-i
    return result

@register_function()
def multlist(var1, var2):
    if type(var1) in (int, float): var1 = [var1 for i in var2]
    elif type(var2) in (int, float): var2 = [var2 for i in var1]
    return [a * b for a, b in zip(var1, var2)]

@register_function()
def divlist(var1, var2):
    if type(var1) in (int, float): var1 = [var1 for i in var2]
    elif type(var2) in (int, float): var2 = [var2 for i in var1]
    return [a / b for a, b in zip(var1, var2)]

@register_function()
def substlist(var1, var2):
    if type(var1) in (int, float): var1 = [var1 for i in var2]
    elif type(var2) in (int, float): var2 = [var2 for i in var1]
    return [a - b for a, b in zip(var1, var2)]

@register_function()
def addlist(var1, var2):
    if type(var1) in (int, float): var1 = [var1 for i in var2]
    elif type(var2) in (int, float): var2 = [var2 for i in var1]
    return [a + b for a, b in zip(var1, var2)]

@register_function()
def sum(var1, last=None):
    total = 0
    if last == None:
        for i in var1: total += i
    else:
        for i in range(0, last): total += var1[0-last]
    return total

# Pinescript Functions
# def convert_code(code): return code.replace("//", "#").replace("0.", "[]").replace("Ãœ","Ü")

@register_function()
def change(var1, var2): return var2-var1

@register_function()
def changeper(var1, var2): return (var2-var1)/var1*100

@register_function()
def roc(var1, var2): return var1[-1]-var1[0-var2]

@register_function()
def avg(var1): return sum(var1)/len(var1)

@register_function()
def covariance(x, y):
    cov = 0.0
    x_avg, y_avg = avg(x), avg(y)
    for i in range(len(x)): cov += (x[i] - x_avg) * (y[i] - y_avg)
    return cov

@register_function()
def variance(var1):
    var1_avg = avg(var1)
    return sum((x - var1_avg) ** 2 for x in var1)

@register_function()
def max(*varies): 
    if type(varies[0]) in (list, tuple, np.ndarray):
        vl = len(varies[0])
        for var in varies: 
            if len(var) != vl: raise "max(): Length of parameters are not equal."
        vt = type(varies[0])
        for var in varies: 
            if type(var) != vt: raise "max(): Type of parameters are not same."
        output = []
        for i in range(0, len(varies[0])):
            hv = -99999999999
            for var in varies:
                if var[i] > hv: hv = var[i]
            output.append(hv)
        return output
    else:
        hv = -99999999999
        for var in varies:
            if var > hv: hv = var
        return hv
       
@register_function()     
def min(*varies): 
    if type(varies[0]) in (list, tuple, np.ndarray):
        vl = len(varies[0])
        for var in varies: 
            if len(var) != vl: raise Exception("min(): Length of parameters are not equal.")
        vt = type(varies[0])
        for var in varies: 
            if type(var) != vt: raise Exception("min(): Type of parameters are not same.")
        output = []
        for i in range(0, len(varies[0])):
            hv = 99999999999
            for var in varies:
                if var[i] < hv: hv = var[i]
            output.append(hv)
        return output
    else:
        hv = 99999999999
        for var in varies: 
            if var < hv: hv = var
        return hv

@register_function()
def highest(var, last=None):
    if not type(var) in (list, tuple, np.ndarray): raise Exception("highest(): Variable is not an array.")
    if last == None: last = len(var)
    hv, hi = -99999999999, -1
    for i in range(0-abs(last), 0):
        if var[i] > hv: hv, hi = var[i], i
    return hv, hi

@register_function()
def lowest(var, last=None):
    if not type(var) in (list, tuple, np.ndarray): raise Exception("lowest(): Variable is not an array.")
    if last == None: last = len(var)
    lv, li = 99999999999, -1
    for i in range(0-abs(last), 0):
        if var[i] < lv: lv, li = var[i], i
    return lv, li

@register_function()
def nz(var1, var2=0):
    output = var1
    if type(var1) in (list, tuple, np.ndarray): 
        for i in range(0, len(output)):
            if pd.isnull(output[i]) or output[i] == None:
                if type(var2) in (list, np.ndarray): output[i] = var2[i]
                else: output[i] = var2
    else: 
        if pd.isnull(output[i]) or output[i] == None: 
            if type(var2) in (list, np.ndarray): output = var2[i]
            else: output = var2
    return output

@register_function()
def stdev(var, last=None): 
    if last == 0: last = len(var)
    return np.std(var[-abs(last):], axis=0)

# @register_function()
# def barssince(): pass

# @register_function()
# def valuewhen(): pass

# Custom

@register_function()
def ray(x, point1, point2):
    """
    #### Example Parameters
    - x      = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    - point1 = (2, 4)
    - point2 = (4, 3)
    """
    output = [np.nan for i in range(len(x))]
    dif = (point2[1]-point1[1])/(x.index(point2[0])-x.index(point1[0]))
    dif = 0-abst(dif) if point1[1] < point2[1] else abst(dif)
    for i in range(x.index(point1[0]), len(x)): output[i] = point1[1] + dif*(x.index(point1[0])-i)
    return output

@register_function()
def linreg(x, y, start=None, end=None):
    if start != None and end != None and start > end:
        start, end = end, start
    out = [np.nan for _ in x]
    if start != None: x, y = x[start:], y[start:]
    if end != None: x, y = x[:end], y[:end]
    b1 = covariance(x, y) / variance(x)
    b0 = avg(y) - b1 * avg(x)
    if start == None: start = 0
    if end == None: end = 0
    for i in range(len(x)): out[i+start] = b0 + b1*x[i]
    return out