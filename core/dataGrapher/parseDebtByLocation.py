import xlrd
import InteractiveMapUnitedStates


workbook = xlrd.open_workbook(f"../../data/Portfolio-by-Location.xls")
sheets = workbook.sheets()
x: xlrd.sheet.Sheet = sheets[0]
place = []
balance = []

# Loop through the data range
for row in range(7, 59):
    place.append(x[row][0])
    balance.append(x[row][1].value)

# Remove Puerto Rico from the dataset.
place.pop(38)
balance.pop(38)

# Create a map from the data
InteractiveMapUnitedStates.create_map(balance)
