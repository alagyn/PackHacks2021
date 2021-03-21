import xlrd


class SummaryData:
    def __init__(self):
        # labels for year and quarter
        self.yearQuartList = []
        # Axis labels with only Q1
        self.yearTicks = []
        # Y vals for historic data
        self.debtVals = []
        # labels for pandemic year and quarter
        self.pandYQ = []
        # Y vals for pandemic data
        self.pandVals = []

    def totalLen(self):
        return len(self.yearQuartList) + len(self.pandYQ)


def getData() -> SummaryData:
    # Open the workbook
    data = xlrd.open_workbook("../../data/GraphingData.xls")
    # Get the sheet
    sheet = data.sheets()[0]
    # Get the columns from the sheet
    yearCol = sheet.col(0)
    quartCol = sheet.col(1)
    debtCol = sheet.col(2)
    recipCol = sheet.col(3)

    # Setup our plotting lists
    data = SummaryData()

    # Iterate through each row, skipping the header
    for idx in range(1, len(yearCol)):
        year = int(yearCol[idx].value)
        quarter = str(quartCol[idx].value)
        # Combine year and quarter
        yq = f"{str(year)}:{quarter}"

        if year < 2020:
            data.yearQuartList.append(yq)
            data.debtVals.append(debtCol[idx].value)
        else:
            data.pandYQ.append(yq)
            data.pandVals.append(debtCol[idx].value)

        # If Q1, append to the x axis ticks
        if quarter == "Q1":
            data.yearTicks.append(yq)

    return data
