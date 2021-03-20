import xlrd
import matplotlib.pyplot as plt
import numpy as np

# Plots a regression of the total debt
if __name__ == "__main__":
    # Open the workbook
    data = xlrd.open_workbook("../../data/GraphingData.xls")
    # Get the sheet
    sheet = data.sheets()[0]
    # Make a plot
    fig, ax = plt.subplots()
    # Get the columns from the sheet
    yearCol = sheet.col(0)
    quartCol = sheet.col(1)
    debtCol = sheet.col(2)
    recipCol = sheet.col(3)

    # Setup our plotting lists
    yearQuartList = []
    yearTicks = []
    debtVals = []
    pandYQ = []
    pandVals = []
    # Iterate through each row, skipping the header
    for idx in range(1, len(yearCol)):
        year = int(yearCol[idx].value)
        quarter = str(quartCol[idx].value)
        # Combine year and quarter
        yq = f"{str(year)}:{quarter}"

        if year < 2020:
            yearQuartList.append(yq)

            # If Q1, append to the x axis ticks
            if quarter == "Q1":
                yearTicks.append(yq)

            debtVals.append(debtCol[idx].value)
        else:
            pandYQ.append(yq)
            if quarter == "Q1":
                yearTicks.append(yq)

            pandVals.append(debtCol[idx].value)

    # range of every year to use in regression
    idxRange = [x for x in range(len(yearQuartList))]
    # get slope/coefficient
    baseCoeff = np.polyfit(idxRange, debtVals, 1)
    # create regression func
    basePolyFunc = np.poly1d(baseCoeff)

    # plot our base data and regression
    ax.plot(yearQuartList, debtVals, '.b')
    ax.plot(yearQuartList, basePolyFunc(idxRange), ':b')

    # do the same to total data
    yearQuartList.extend(pandYQ)
    debtVals.extend(pandVals)
    idxRange = [x for x in range(len(yearQuartList))]

    pCoeff = np.polyfit(idxRange, debtVals, 1)
    pPolyFunc = np.poly1d(pCoeff)

    # plot pandemic data
    ax.plot(pandYQ, pandVals, "r.")
    s = -len(pandYQ) - 1
    ax.plot(yearQuartList[s:], pPolyFunc(idxRange[s:]), '--y')

    plt.xticks(yearTicks)

    plt.show()
