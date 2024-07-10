from setuptools import setup, find_packages
setup(
    name='pinetwig',
    version='0.1.1',
    author='Ayberk ATALAY',
    author_email='ayberkatalaypersonal@gmail.com',
    description='A pinescript-like financial data analysis package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)