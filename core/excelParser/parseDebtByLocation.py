import xlrd

from core.dataGrapher import InteractiveMapUnitedStates

if __name__ == "__main__":

    for num in range(4):
        workbook = xlrd.open_workbook(f"../../data/Portfolio-by-Location ({num}).xls")

        sheets = workbook.sheets()

        x: xlrd.sheet.Sheet = sheets[0]

        place = []
        balance = []
        for row in range(7, 59):
            place.append(x[row][0])
            balance.append(x[row][1].value)

        # Remove Puerto Rico from the dataset.
        place.pop(38)
        balance.pop(38)

        InteractiveMapUnitedStates.create_map(balance, num)
