from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
def getvalue(x): return x.value
list_x=list(map(getvalue, sheet['A'][1:]))
sheet['C'][1:]
list_y=list(map(getvalue, sheet['D'][1:]))
sheet['D'][1:]
list_z=list(map(getvalue, sheet['C'][1:]))
pyplot.plot(list_x, list_y)
pyplot.plot(list_x, list_z)
pyplot.show()