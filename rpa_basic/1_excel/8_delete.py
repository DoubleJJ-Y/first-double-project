from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# #8행부터 3개 행 삭제
# ws.delete_rows(8,3)

# #8열 부터 2개 열 삭제
# ws.delete_cols(2,2)

wb.save("sample_delete.xlsx")