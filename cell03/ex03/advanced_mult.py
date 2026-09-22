#!/usr/bin/env python3
import sys

# ถ้ามีการส่ง arguments มา (เช่น รันแล้วใส่ข้อความเพิ่ม) ให้แสดงคำว่า none และจบโปรแกรม
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        # พิมพ์หัวข้อของแต่ละแม่สูตรคูณ
        output = "Table de " + str(i) + ":"
        j = 0
        while j <= 10:
            output += " " + str(i * j)
            j += 1
        print(output)
        i += 1