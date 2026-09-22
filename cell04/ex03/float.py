#!/usr/bin/env python3

# รับค่าเป็นข้อความจากผู้ใช้เพื่อตรวจสอบจุดทศนิยม
user_input = input("Give me a number: ")

# ตรวจสอบว่าในข้อความมีจุดทศนิยมหรือไม่
if "." in user_input:
    print("This number is a decimal.")
else:
    print("This number is an integer.")