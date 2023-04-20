# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:37:58 2023

@author: ander.alvarez
"""

import xlwings as xw


# Open the Excel file
wb = xw.Book('baseball_stadiumsxlsx')

# Select the sheet
sheet = wb.sheets['Sheet1']

# Import the first two columns of data
stadiums = sheet.range('A2:A31').value
cities = sheet.range('B2:B31').value
lats = sheet.range('C2:C31').value
longs = sheet.range('D2:D31').value


# Print the data to the console
print(stadiums)
print(cities)
print(lats)
print(longs)
