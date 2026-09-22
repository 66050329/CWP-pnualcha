#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นจำนวนเต็ม
number = int(input())

# วนลูปตั้งแต่ 0 ถึง 9 เพื่อแสดงสูตรคูณ
for i in range(10):
    print(f"{i} * {number} = {i * number}")