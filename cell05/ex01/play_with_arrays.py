#!/usr/bin/env python3
#แสดงผลอาร์เรย์ที่กำหนดไว้และสร้างอาร์เรย์ใหม่โดยบวก 2 เข้าไปในแต่ละค่า
# 1. กำหนดอาร์เรย์ตั้งต้น (original array)
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. วนลูปเพื่อสร้างอาร์เรย์ใหม่โดยบวก 2 เข้าไปในแต่ละค่า[cite: 6]
new_array = [x + 2 for x in original_array]

# 3. แสดงผลทั้งสองอาร์เรย์บนหน้าจอตามรูปแบบที่กำหนด[cite: 6]
print("Original array:", original_array)
print("New array:", new_array)