import parseSummaryData
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import sys
from rsquared import rSquared

# Plots a regression of the total debt
if __name__ == "__main__":
    if len(sys.argv) != 2:
        polyDegree = int(input("Please enter a polynomial degree > "))
    else:
        polyDegree = int(sys.argv[1])

    dataset = int(input("1: Debt, 2: Recipients > "))

    # get our data
    data = parseSummaryData.getData(dataset)

    # Setup plot
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # Title and axi labels
    ax.set_title(f"{data.title}, Polynomial Degree: {polyDegree}")
    ax.set_xlabel("Yearly Quarters")
    ax.set_ylabel(data.yAxis)
    ax.yaxis.set_tick_params(which='major', labelcolor='green')
    # Grid
    ax.grid(True, linestyle='-.')

    # range of every year to use in regression
    idxRange = [x for x in range(len(data.baseYQ))]
    # get slope/coefficient
    baseCoeff = np.polyfit(idxRange, data.baseVals, polyDegree)
    # create regression func
    basePolyFunc = np.poly1d(baseCoeff)

    # plot our base data and regression

    ax.plot(data.baseYQ, data.baseVals, '.b')
    # ax.plot(data.yearQuartList, basePolyFunc(idxRange), ':b')
    baseRS = rSquared(data.baseVals, basePolyFunc(idxRange))
    oldRegLine = lines.Line2D(idxRange, basePolyFunc(idxRange), color='b', marker='', linestyle=':',
                              label=f"{data.yAxis}, R^2: {baseRS:2.3f}")
    ax.add_line(oldRegLine)

    # do the same to total data
    data.baseYQ.extend(data.pandYQ)
    data.baseVals.extend(data.pandVals)
    idxRange = [x for x in range(len(data.baseYQ))]

    pCoeff = np.polyfit(idxRange, data.baseVals, polyDegree)
    pPolyFunc = np.poly1d(pCoeff)

    # plot pandemic data
    ax.plot(data.pandYQ, data.pandVals, "r.")
    s = -len(data.pandYQ) - 1
    # ax.plot(data.yearQuartList[s:], pPolyFunc(idxRange[s:]), '--r')
    pandRS = rSquared(data.baseVals, pPolyFunc(idxRange))
    pandRegLine = lines.Line2D(idxRange[s:], pPolyFunc(idxRange[s:]), color='r', marker='', linestyle=':',
                               label=f"Pandemic Debt, R^2: {pandRS:2.3f}")
    ax.add_line(pandRegLine)

    ax.legend(handles=[oldRegLine, pandRegLine])

    plt.xticks(data.yearTicks)

    plt.show()
