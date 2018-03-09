#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test the creation of figures with many Keplerians! """

import pytest

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import numpy as np

from keplerian import keplerian


# @pytest.mark.skip(reason="pytest-mpl has problems on Travis...")
@pytest.mark.mpl_image_compare
def test_simple_fig():
    """ Simple figure """
    t = np.linspace(0, 10, 1000)
    P, K, e, w, T0 = 4., 1., 0., 0., 2.
    vsys = 1.
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(t, keplerian(t, P, K, e, w, T0, vsys), lw=2)
    return fig


# @pytest.mark.skip(reason="pytest-mpl has problems on Travis...")
@pytest.mark.mpl_image_compare
def test_complicated_fig():
    """ Not so simple figure """
    t = np.linspace(0, 10, 1000)

    fig, axes = plt.subplots(5, 4)
    for ax in axes.flatten():
        ax.axis('off')
    P, K, T0 = 4., 1., 2
    vsys = 0
    for i, e in enumerate(np.arange(0, 1, 0.2)):
        for j, w in enumerate(np.arange(0, 2*np.pi, np.pi/2)):
            ax = axes[i,j]
            
            kep = keplerian(t, P, K, e, w, T0, vsys)
            ax.plot(t, kep, lw=2)

            ax.axhline(y=0, lw=1, color='k')
            ax.set(ylim=[-2, 2], title='e=%.1f, w=%.2f' % (e, w))

    fig.tight_layout()
    return fig


