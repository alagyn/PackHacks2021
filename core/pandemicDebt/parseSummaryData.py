import xlrd


class SummaryData:
    def __init__(self):
        # labels for year and quarter
        self.baseYQ = []
        # Axis labels with only Q1
        self.yearTicks = []
        # Y vals for historic data
        self.baseVals = []
        # labels for pandemic year and quarter
        self.pandYQ = []
        # Y vals for pandemic data
        self.pandVals = []

        # Axis names
        self.yAxis = ''
        # Data Title
        self.title = ''

    def totalLen(self):
        return len(self.baseYQ) + len(self.pandYQ)


DEBT = 1
RECIP = 2


def getData(column) -> SummaryData:
    # Open the workbook
    data = xlrd.open_workbook("../../data/GraphingData.xls")
    # Get the sheet
    sheet = data.sheets()[0]
    # Get the columns from the sheet
    yearCol = sheet.col(0)
    quartCol = sheet.col(1)
    dataCol = sheet.col(column + 1)

    # Setup our plotting lists
    data = SummaryData()

    if column == DEBT:
        data.yAxis = "Debt (in billion dollars)"
        data.title = "Outstanding Loan Amounts"
    elif column == RECIP:
        data.yAxis = "Recipients (in millions)"
        data.title = "Total Loan Recipients"

    # Iterate through each row, skipping the header
    for idx in range(1, len(yearCol)):
        year = int(yearCol[idx].value)
        quarter = str(quartCol[idx].value)
        # Combine year and quarter
        yq = f"{str(year)}:{quarter}"

        if year < 2020:
            data.baseYQ.append(yq)
            data.baseVals.append(dataCol[idx].value)
        else:
            data.pandYQ.append(yq)
            data.pandVals.append(dataCol[idx].value)

        # If Q1, append to the x axis ticks
        if quarter == "Q1":
            data.yearTicks.append(yq)

    return data
