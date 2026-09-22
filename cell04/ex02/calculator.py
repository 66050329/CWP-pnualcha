#!/usr/bin/env python3

# รับค่าตัวเลขสองจำนวนจากผู้ใช้และแปลงเป็นตัวเลข (int ในตัวอย่างเป็นจำนวนเต็ม)
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

print("Thank you!")

# แสดงผลการบวก ลบ หาร คูณ ตามรูปแบบในตัวอย่าง
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 // num2}")  # ใช้ // หรือ / ตามต้องการ (ในรูปตัวอย่างเป็นหารลงตัว)
print(f"{num1} * {num2} = {num1 * num2}")