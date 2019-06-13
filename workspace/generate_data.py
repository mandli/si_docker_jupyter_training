#!/usr/bin/env python

import numpy
import scipy.interpolate as interpolate

import matplotlib.pyplot as plt

N = 100
t = numpy.linspace(0.0, 1.0, N)
y = t + numpy.random.random((N)) + numpy.sin(numpy.pi * t) + 1

with open('data.txt', 'w') as data_file:
    for i in range(N):
        data_file.write("%s, %s\n" % (t[i], y[i]))

# A = numpy.vander(t, N=5)
# p = numpy.linalg.solve(numpy.dot(A.transpose(), A), numpy.dot(A.transpose(), y))
# f = lambda t: p[4] + p[3] * t + p[2] * t**2 + p[1] * t**3 + p[0] * t**4
f = interpolate.interp1d(t, y, bounds_error=False)

fig, axes = plt.subplots(1, 1)
t_fine = numpy.linspace(0.0, 1.5, 1000)
axes.plot(t, y, 'ko')
axes.plot(t_fine, f(t_fine), 'r')
axes.plot(t_fine[-1], f(t_fine[-1]), 'bs')
axes.set_title("Future Flow")
axes.set_xlabel("t (days)")
axes.set_ylabel(r"Flow $m^3 / s$")
plt.show()