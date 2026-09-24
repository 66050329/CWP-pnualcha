#!/usr/bin/env python3

# 1. กำหนดอาร์เรย์ตั้งต้น[cite: 6]
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้างเซตโดยเลือกเฉพาะค่าที่มากกว่า 5, บวกด้วย 2, และตัดตัวซ้ำออกอัตโนมัติ[cite: 6]
new_set = {x + 2 for x in original_array if x > 5}

# 3. แสดงผลอาร์เรย์เดิมและผลลัพธ์[cite: 6]
print(original_array)
print(new_set)