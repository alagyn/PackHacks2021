import xlrd

if __name__ == "__main__":
    workbook = xlrd.open_workbook("../../data/GraphingData.xls")

    sheets = workbook.sheets()

    x: xlrd.sheet.Sheet = sheets[0]

    print("0,0: " + str(x.cell(0, 0).value))
    print("1,0: " + str(x.cell(1, 0).value))
    print("2,0: " + str(x.cell(2, 0).value))
    print("3,0: " + str(x.cell(3, 0).value))
    print("4,0: " + str(x.cell(4, 0).value))
    print("5,0: " + str(x.cell(5, 0).value))
