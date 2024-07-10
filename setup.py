from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'A pinescript-like financial data analysis package'

print("PACKAGES", find_packages())

setup(
    name='pinetwig',
    author='Ayberk ATALAY',
    author_email='ayberkatalaypersonal@gmail.com',
    description=DESCRIPTION,
    py_modules=['pinetwig'],
    packages=find_packages(), #["__init__", "data", "functions", "indicators", "modules"],
    version=VERSION,
    license='MIT',
    url='https://github.com/AyberkAtalay0/pinetwig',
    keywords=['python', 'pinetwig', 'financial', 'data', 'analysis', 'tradingview', 'binance', 'pinescript', 'trading', 'cryptocurrency'],
    install_requires=[
        'pandas',
        'numpy',
        'python-binance',
        'websocket',
        'datetime'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)