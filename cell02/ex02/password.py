# กำหนดรหัสผ่านตามโจทย์[cite: 1] นี่คือรหัสผ่านที่ถูกต้องสำหรับการเข้าถึงระบบ
password = "Python is awesome"

# รับค่ารหัสผ่านจากผู้ใช้[cite: 1]
entered_password = input()

# ตรวจสอบเงื่อนไข[cite: 1]
if entered_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")