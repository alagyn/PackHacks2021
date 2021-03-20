import xlrd

if __name__ == "__main__":
    workbook = xlrd.open_workbook("../../data/fafsa-demographics-2017-18.xls")

    print(f'Worksheets: {workbook.nsheets}')

    sheets = workbook.sheets()

    x: xlrd.sheet.Sheet
    for x in sheets:
        print(f"{x.name}: lines: {x.nrows}")
