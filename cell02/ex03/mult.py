#!/usr/bin/env python3

# รับค่าตัวเลขสองจำนวนจากผู้ใช้ พร้อมแสดงข้อความบอก
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# คำนวณผลคูณ
result = num1 * num2

# ตรวจสอบว่าผลคูณเป็น บวก, ลบ, หรือศูนย์
if result > 0:
    print("Positive")#ถ้าคูณแล้วเป็นบวก
elif result < 0:
    print("Negative")#ถ้าคูณแล้วเป็นลบ
else:
    print("Zero")#ถ้าคูณแล้วเป็นศูนย์

# แสดงผลลัพธ์ของการคูณ
print(result)