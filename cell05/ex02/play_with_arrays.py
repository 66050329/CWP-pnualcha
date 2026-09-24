#!/usr/bin/env python3

# 1. กำหนดอาร์เรย์ตั้งต้น
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้างอาร์เรย์ใหม่โดยเลือกเฉพาะค่าที่มากกว่า 5 แล้วบวกด้วย 2
new_array = [x + 2 for x in original_array if x > 5]

# 3. แสดงผลทั้งสองอาร์เรย์ตามรูปแบบที่โจทย์ต้องการ
print(original_array)
print(new_array)