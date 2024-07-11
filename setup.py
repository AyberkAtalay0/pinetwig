from setuptools import setup, find_packages

VERSION = '0.2.1'
DESCRIPTION = 'A pinescript-like financial data analysis and trading package'

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pinetwig',
    author='Ayberk ATALAY',
    author_email='ayberkatalaypersonal@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description=DESCRIPTION,
    py_modules=['pinetwig'],
    packages=find_packages(),
    version=VERSION,
    license='MIT',
    url='https://github.com/AyberkAtalay0/pinetwig',
    keywords=['python', 'pinetwig', 'financial', 'data', 'analysis', 'tradingview', 'binance', 'pinescript', 'trading', 'cryptocurrency', 'chart', 'candlestick', 'plotly', 'matplotlib', 'visualizing'],
    install_requires=[
        'pandas',
        'numpy',
        'python-binance',
        'websocket-client',
        'websockets',
        'datetime',
        'plotly',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>= 3.6',
)
