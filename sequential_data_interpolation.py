# -*- coding: utf-8 -*-
#python3
#Author: Yanan Liu
# @Time    : 11/01/2022 10:28
# @Software: PyCharm 
# @File    : sequential_data_interpolation

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot


def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')


data_path = "E:/Career/ShU/shampoo.csv"

series = read_csv(data_path, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
series.plot()
pyplot.show()


series = read_csv(data_path, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
upsampled = series.resample('D')
interpolated = upsampled.interpolate(method='spline', order=2)
print(interpolated.head(32))
interpolated.plot()
pyplot.show()



