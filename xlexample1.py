from xlrd import open_workbook

#simple xlrd usage
#program reads contents of xl file and displays

book = open_workbook('sample.xls')
print book.nsheets

for sheet_index in range(book.nsheets):
	print book.sheet_by_index(sheet_index)

print book.sheet_names()
for sheet_name in book.sheet_names():
	print book.sheet_by_name(sheet_name)
	
	
for sheet in book.sheets():
	print sheet
	
ISE_sheet  = book.sheet_by_index(4)

print ISE_sheet.col_values(1,2)

