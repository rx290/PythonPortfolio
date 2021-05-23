we have many resources to read and write excel files, some of which are as followS:
	1. Openpyxl
	2. xlsxwriter
	3. pyxlsb
	4. pylightxl
	5. xlrd
	6. xlwt
	7. xlutils

# Openpyxl

Openpyxl is the recommended way to manipulate excel files.

# xlsxwriter

it is an alternate to Openpyxl but apart from that it has data formatting and charting capability according to the 2010 MS Excel

# pyxlsb

a package to manipulate xlsb extensions

# pylightxl

a package to manipulate sx and sm files

# xlrd and xlwt

first one is the package to read data from older excel files on the other hand xlwt is a package to write to older excel files

# xlutils

a package which can utileze both xlrd and xlwt along with the attributes of modifying, copy/paste and filtering excel files

# Usage

to create a work book simply import the Workbook module from openpyxl

then initiate the object to some variable and run var.activate attribute

## creating a workbook

to create a workbook we simply need to invoke create attribute

like ws1 = wb.create_sheet('name')

## saving a workbook

to save a work book we have to invoke save attribute like

wb.save('name.xlxs')

## creating Tables

for creating tables we must define a selected table which can be done by using nested loops

eg:
	for x in range(1,11):
		for y in range(1,11):
			ws.cell(row=x,column=y)

columns = list(range(0,10))

for col in ws.iter_cols(min_col = 0, max_cols=3, max_rows=5):
	for cell in col:
	ws.append(columns)

## Merging cells

TO merge cells one must follow this step:
w2.merge_cells('slice')

## Reading from excel files

