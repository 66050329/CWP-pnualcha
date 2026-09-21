#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นประเภท float (หรือ int)
number = float(input("Enter a number: "))

# ตรวจสอบเงื่อนไขตามโจทย์
if number < 0:
    print("This number is negative.")#เมื่อค่าติดลบ
elif number > 0:
    print("This number is positive.")#เมื่อค่าเป็นบวก
else:
    print("This number is both positive and negative.")#เมื่อค่าเป็น0