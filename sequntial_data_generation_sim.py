# -*- coding: utf-8 -*-
#python3
#Author: Yanan Liu
# @Time    : 18/01/2022 11:30
# @Software: PyCharm 
# @File    : sequntial_data_generation_sim

import numpy as np
import timesynth as ts
import pandas as pd
from scipy import interpolate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


# Initializing TimeSampler
time_sampler = ts.TimeSampler(stop_time=20)
# Sampling irregular time samples
irregular_time_samples = time_sampler.sample_irregular_time(num_points=50, keep_percentage=50)
# Initializing Sinusoidal signal
sinusoid = ts.signals.Sinusoidal(frequency=5)
# Initializing Gaussian noise
white_noise = ts.noise.GaussianNoise(std=0.3)
# Initializing TimeSeries class with the signal and noise objects
timeseries = ts.TimeSeries(sinusoid, noise_generator=white_noise)
# Sampling using the irregular time samples
samples, signals, errors = timeseries.sample(irregular_time_samples)

#####pandas
# using simulated samples for fitting and interpolation
# test_gap = 10
# sim_sample = np.zeros(samples.size*10)
# for i in range(sim_sample.size):
#     sim_sample[i] = np.nan
# k = 0
# for j in range(0, sim_sample.size, test_gap):
#     sim_sample[j] = samples[k]
#     k = k+1
# # convert to pandas dataframe for interpolation
# df = pd.DataFrame(sim_sample)
# interpolated_polynomial = df.interpolate(method='polynomial', order=2)
# interpolated_linear = df.interpolate(method='linear')

###scipy
x = [i for i in range(samples.size)]
fit_linear = interp1d(x, samples, kind="linear")
fit_cubic = interp1d(x, samples, kind='cubic')
fit_quad = interp1d(x, samples, kind='quadratic')
fit_akima = interpolate.Akima1DInterpolator(x, samples)

x_test = np.linspace(0,samples.size-1,4000)

# cubic Hermite interpolation
y_test = interpolate.pchip_interpolate(x, samples, x_test)

plt.plot(samples, 'o')
plt.plot(x_test, fit_linear(x_test))
plt.plot(x_test, fit_cubic(x_test))
plt.plot(x_test, fit_quad(x_test))
plt.plot(x_test, y_test)
plt.plot(x_test, fit_akima(x_test))
plt.legend(["Given Data", "Interpolation (Linear)", "Interpolation (Cubic) ",
            "Interpolationo (Quad)", 'Interpolationo (Hermite)', 'Interpolation (Akima)'], loc ="lower right")
plt.grid()
plt.show()


# plt.plot(interpolated_polynomial)
