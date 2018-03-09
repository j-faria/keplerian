# -*- coding: utf-8 -*-

import numpy as np 
pi = np.pi

from .eccentric_anomaly import ecc_anomaly1 as ecc_anomaly

def keplerian(time, p, k, ecc, omega, t0, vsys):
    vel = np.zeros_like(time)
    p, k, ecc, omega, t0 = np.atleast_1d(p, k, ecc, omega, t0)

    for i in range(p.size):
        M = 2.*pi * (time-t0[i]) / p[i]
        E = ecc_anomaly(M, ecc[i])
        nu = true_anomaly(E, ecc[i])
        vel += k[i] * (np.cos(omega[i]+nu) + ecc[i]*np.cos(omega[i]))
    vel += vsys
    return vel

def true_anomaly(E, e):
    return 2. * np.arctan( np.sqrt((1.+e)/(1.-e)) * np.tan(E/2.))

