from __future__ import division
import numpy as np
import pandas as pd
import os, argparse
from sklearn.grid_search import GridSearchCV
from sklearn.neighbors import KernelDensity
import  matplotlib.pyplot as plt
from scipy.misc import comb

mydir = os.path.expanduser('~/github/Evol_16S/')

def CV_KDE(oneD_array):
    # remove +/- inf
    oneD_array = oneD_array[np.logical_not(np.isnan(oneD_array))]
    grid = GridSearchCV(KernelDensity(),
                    {'bandwidth': np.logspace(0.1, 5.0, 30)},
                    cv=20) # 20-fold cross-validation
    grid.fit(oneD_array[:, None])
    x_grid = np.linspace(np.amin(oneD_array), np.amax(oneD_array), 10000)
    kde = grid.best_estimator_
    pdf = np.exp(kde.score_samples(x_grid[:, None]))
    # returns grod for x-axis,  pdf, and bandwidth
    return_tuple = (x_grid, pdf, kde.bandwidth)
    return return_tuple

def plotSeqSubRate():
    siteRates =  np.loadtxt(open(mydir + 'Tree/data/rates/siteRate.txt',"rb"),delimiter=",",skiprows=1)
    rates = siteRates[:,0]
    x = range(1, len(rates) + 1)
    fig, ax = plt.subplots()
    plt.plot(x, rates, marker='o')
    ax.set_xlabel('16S rRNA position', fontsize = 16  )
    ax.set_ylabel('Substitutions (rate * tree length)', fontsize = 16)
    plt.savefig(mydir + 'Simulation/figs/SeqSubRates1.png', dpi=600,)
    plt.close()

    fig, ax = plt.subplots()
    plt.plot(x, rates, marker='o')
    #fig, ax = plt.subplots()
    plt.ylim(0,6)
    ax.set_xlabel('16S rRNA position', fontsize = 16  )
    ax.set_ylabel('Substitutions (rate * tree length)', fontsize = 16)
    plt.savefig(mydir + 'Simulation/figs/SeqSubRates2.png', dpi=600,)
    plt.close()




def plotSubRate():
    siteRates =  np.loadtxt(open(mydir + 'Tree/data/rates/siteRate.txt',"rb"),delimiter=",",skiprows=1)
    rates = siteRates[:,0]
    print len(rates)
    #KDE = CV_KDE(rates)
    fig, ax = plt.subplots()
    #ax.plot(KDE[0], KDE[1], linewidth=3, alpha=0.5, label='bw=%.2f' % KDE[2])
    #ax.hist(rates, 100, fc='gray', histtype='stepfilled', alpha=0.3, normed=True)
    ax.hist(rates, 30, fc='gray', histtype='stepfilled', alpha=0.5, normed=False)
    ax.set_xlabel('Substitutions (rate * tree length)', fontsize = 16  )
    ax.set_ylabel('Number of sites', fontsize = 16)
    ax.text(2, 1650, 'Site-specific substitutions in the 16S rRNA gene ', fontsize=15)
    #ax.legend(loc='upper left')
    plt.savefig(mydir + 'Simulation/figs/SubRates.png', dpi=600,)
    plt.close()


def binomFig():
    fig, ax = plt.subplots()
    N = 1000
    x = []
    y = []
    for j in range(1, N+1):
        binSample = comb(N,j)*(0.25)**j*(0.75)**(N-j)
        x.append(j)
        y.append(binSample)
        print binSample
    plt.plot(x, y, marker='o')
    plt.savefig(mydir + 'Simulation/figs/Binom.png', dpi=600,)
    plt.close()


plotSubRate()