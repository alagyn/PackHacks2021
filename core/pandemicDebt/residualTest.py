import scipy.stats as sp
import matplotlib.pyplot as plt
import matplotlib.lines as mLines
import parseSummaryData
import numpy as np
import sys
from rsquared import rSquared

if __name__ == "__main__":
    if len(sys.argv) != 2:
        polyDegree = int(input("Please enter a polynomial degree > "))
    else:
        polyDegree = int(sys.argv[1])

    dataset = int(input("1: Debt, 2: Recipients > "))

    # get our data
    data = parseSummaryData.getData(dataset)

    # range of every year to use in regression
    idxRange = [x for x in range(len(data.baseYQ))]
    # get estimate regression
    coeff = np.polyfit(idxRange, data.baseVals, polyDegree)
    regLine = np.poly1d(coeff)

    rsquare = rSquared(data.baseVals, regLine(idxRange))

    # Calculate residuals
    baseResiduals = []

    for x in idxRange:
        observed = data.baseVals[x]
        expected = regLine(x)
        baseResiduals.append(observed - expected)

    # calc standard deviation of residuals
    residualSD = sp.tstd(baseResiduals)
    # calc standardized residuals
    stdResiduals = [x / residualSD for x in baseResiduals]

    # do it again for the pandemic data using the historic regression line
    pandIdx = range(len(idxRange), len(idxRange) + len(data.pandYQ))
    pandResiduals = []

    totalResid = baseResiduals.copy()

    for idx in range(len(data.pandYQ)):
        observed = data.pandVals[idx]
        expected = regLine(pandIdx[idx])
        pandResiduals.append(observed - expected)
        totalResid.append(observed - expected)

    # pandResidSD = sp.tstd(totalResid)
    pandResidSD = residualSD
    stdPandResid = [x / pandResidSD for x in pandResiduals]

    # Make plot
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.set_title(f"{data.title}: Standardized Residuals, Polynomial Degree: {polyDegree}")
    ax.grid(True, linestyle='-.')
    ax.set_ylabel("Residual / Standard Deviation of all Residuals")

    # Plot historic resids
    baseLine = mLines.Line2D(idxRange, stdResiduals, marker='.', linestyle='', color='b',
                             label=f'Historic Debt, R^2: {rsquare:2.3f}')
    # Plot pandemic resids
    pandLine = mLines.Line2D(pandIdx, stdPandResid, marker='p', linestyle='', color='r',
                             label='Pandemic Debt')

    ax.add_line(baseLine)
    ax.add_line(pandLine)

    # Setup viewport range
    xmin = -1
    xmax = idxRange[-1] + len(pandIdx) + 1
    # Add significance lines
    ax.hlines(y=[-2, 2], xmin=xmin, xmax=xmax, label='2 * Standard Deviation')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-5, 5)

    plt.xticks([x for x in range(0, data.totalLen(), 4)], data.yearTicks)

    ax.legend()

    ax.plot()

    plt.show()

