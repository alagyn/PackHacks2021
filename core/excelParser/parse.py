import xlrd

if __name__ == "__main__":
    workbook = xlrd.open_workbook("../../data/fafsa-demographics-2017-18.xls")

    print(f'Worksheets: {workbook.nsheets}')

    sheets = workbook.sheets()

    x: xlrd.sheet.Sheet = sheets[0]

    for rowNum in range(x.nrows):
        row = x.row(rowNum)
        line = "".join(str(cell.value) + "," for cell in row)
        print(line)

