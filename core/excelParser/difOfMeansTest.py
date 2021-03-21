import scipy.stats as sp
import matplotlib.pyplot as plt
import matplotlib.lines as mLines
import parseSummaryData


def parseRegData(reg):
    out = f"Slope: {reg.slope}\n"
    out += f"Intercept: {reg.intercept}\n"
    out += f"R-Squared: {reg.rvalue}\n"
    out += f"StdErr: {baseReg.stderr}\n"
    out += f"Intercept StdErr: {baseReg.intercept_stderr}\n"
    return out


class Line:
    def __init__(self, inter, slope):
        self.inter = inter
        self.slope = slope

    '''Returns the estimated Y value for the passed X value'''

    def __call__(self, xVal) -> float:
        return self.inter + self.slope * xVal


if __name__ == "__main__":
    data = parseSummaryData.getData()

    # range of every year to use in regression
    idxRange = [x for x in range(len(data.yearQuartList))]
    # get estimate regression
    baseReg = sp.linregress(idxRange, data.debtVals)

    # setup line object
    regLine = Line(baseReg.intercept, baseReg.slope)

    # Calculate residuals
    baseResiduals = []

    for x in idxRange:
        observed = data.debtVals[x]
        expected = regLine(x)
        baseResiduals.append(observed - expected)

    # calc standard deviation of residuals
    residualSD = sp.tstd(baseResiduals)
    # calc standardized residuals
    stdResiduals = [x / residualSD for x in baseResiduals]

    # do it again for the pandemic data using the historic regression line
    pandIdx = range(len(idxRange), len(idxRange) + len(data.pandYQ))
    pandResiduals = []

    for idx in range(len(data.pandYQ)):
        observed = data.pandVals[idx]
        expected = regLine(pandIdx[idx])
        resid = observed - expected
        pandResiduals.append(resid)

    # pandResidSD = sp.tstd(totalResid)
    pandResidSD = residualSD
    stdPandResid = [x / pandResidSD for x in pandResiduals]

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.set_title("Standardized Residuals")
    ax.grid(True, linestyle='-.')

    # Plot historic resids
    baseLine = mLines.Line2D(idxRange, stdResiduals, marker='.', linestyle='', color='b',
                             label='Historic Debt')
    # Plot pandemic resids
    pandLine = mLines.Line2D(pandIdx, stdPandResid, marker='p', linestyle='', color='r',
                             label='Pandemic Debt')

    ax.add_line(baseLine)
    ax.add_line(pandLine)

    xmin = -1
    xmax = idxRange[-1] + len(pandIdx) + 1


    ax.hlines(y=[-2,2], xmin=xmin, xmax=xmax, label='2 * Standard Deviation')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-5, 5)

    plt.xticks([x for x in range(0, data.totalLen(), 4)], data.yearTicks)

    # ax.legend(handles=[baseLine, pandLine])
    ax.legend()

    ax.set_ylabel("Residual / Standard Deviation of all Residuals")

    ax.plot()

    plt.show()
