from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#8행에 빈행을 추가
ws.insert_rows(8)
#8행 5줄 추가
ws.insert_rows(8,5)

#B 번째에 빈열 추가
ws.insert_cols(2,3) #B열 부터 3열 추가

wb.save("sample_insert.xlsx")