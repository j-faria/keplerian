# -*- coding: utf-8 -*-
import numpy as np
pi = np.pi

DERROR = 1e-10

def ecc_anomaly1(M, e):
    # catch special case
    if isinstance(e, float) and e == 0.0:
        return M

    M = np.atleast_1d(M)
    E0 = M; E = M
    for _ in range(200):
        g = E0 - e * np.sin(E0) - M
        gp = 1.0 - e * np.cos(E0)
        E = E0 - g / gp

        # convergence?
        if (np.linalg.norm(E - E0, ord=1) <= DERROR): 
            return E
        # not yet
        E0 = E

    # no convergence, return the best estimate
    return E

