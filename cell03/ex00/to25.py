#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นตัวเลขจำนวนเต็ม
number = int(input())

# ตรวจสอบว่าตัวเลขมากกว่า 25 หรือไม่
if number > 25:
    print("Error")
else:
    # วนลูปแสดงตัวเลขจากค่าที่รับเข้ามาจนถึง 25
    for i in range(number, 26):
        print(i)