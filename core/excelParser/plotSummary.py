import parseSummaryData
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

# Plots a regression of the total debt
if __name__ == "__main__":
    # get our data
    data = parseSummaryData.getData()

    # Make a plot
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.set_title("Outstanding Loan Amounts")
    ax.set_xlabel("Yearly Quarters")
    ax.set_ylabel("Debt (in billion dollars)")
    ax.yaxis.set_major_formatter('${x:1.2f}')
    ax.yaxis.set_tick_params(which='major', labelcolor='green')



    ax.grid(True, linestyle='-.')

    # range of every year to use in regression
    idxRange = [x for x in range(len(data.yearQuartList))]
    # get slope/coefficient
    baseCoeff = np.polyfit(idxRange, data.debtVals, 1)
    # create regression func
    basePolyFunc = np.poly1d(baseCoeff)

    # plot our base data and regression

    ax.plot(data.yearQuartList, data.debtVals, '.b')
    # ax.plot(data.yearQuartList, basePolyFunc(idxRange), ':b')
    oldRegLine = lines.Line2D(idxRange, basePolyFunc(idxRange), color='b', marker='', linestyle=':',
                              label="Historic debt")
    ax.add_line(oldRegLine)

    # do the same to total data
    data.yearQuartList.extend(data.pandYQ)
    data.debtVals.extend(data.pandVals)
    idxRange = [x for x in range(len(data.yearQuartList))]

    pCoeff = np.polyfit(idxRange, data.debtVals, 1)
    pPolyFunc = np.poly1d(pCoeff)

    # plot pandemic data
    ax.plot(data.pandYQ, data.pandVals, "r.")
    s = -len(data.pandYQ) - 1
    # ax.plot(data.yearQuartList[s:], pPolyFunc(idxRange[s:]), '--y')
    pandRegLine = lines.Line2D(idxRange[s:], pPolyFunc(idxRange[s:]), color='y', marker='', linestyle=':',
                               label="Pandemic Debt")
    ax.add_line(pandRegLine)

    ax.legend(handles=[oldRegLine, pandRegLine])

    plt.xticks(data.yearTicks)

    plt.show()
