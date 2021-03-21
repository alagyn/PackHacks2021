import scipy.stats as sp
import matplotlib.pyplot as plt
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
        pandResiduals.append(observed - expected)

    pandResidSD = sp.tstd(pandResiduals)
    stdPandResid = [x / pandResidSD for x in pandResiduals]

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.set_title("Standardized Residuals")

    # Plot historic resids
    ax.plot(idxRange, stdResiduals, '.b')
    # Plot pandemic resids
    ax.plot(pandIdx, stdPandResid, '.r')

    plt.show()
