#!/usr/bin/env python3

# รับค่าข้อความแรกจากผู้ใช้ก่อนเข้าลูป
user_input = input("What you gotta say? : ")

# วนลูปทำงานไปเรื่อยๆ จนกว่าผู้ใช้จะพิมพ์คำว่า STOP
while user_input != "STOP":
    user_input = input("I got that! Anything else? : ")