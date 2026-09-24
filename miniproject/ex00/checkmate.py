def checkmate(board):
    # ขั้นตอนที่ 1: ตรวจสอบว่ากระดานว่างเปล่าหรือไม่ ถ้าว่างให้จบการทำงานทันที
    if not board:
        print("Fail")
        return

    # ขั้นตอนที่ 2: แปลงข้อความกระดานให้ออกมาเป็นแถวๆ และวัดขนาดความกว้าง/ยาวของกระดาน
    rows = board.splitlines()
    size = len(rows)

    # ขั้นตอนที่ 3: ตรวจสอบว่าขนาดของกระดานแต่ละแถวเท่ากันหรือไม่ (ต้องเป็นสี่เหลี่ยมจัตุรัส)
    if any(len(row) != size for row in rows):
        print("ขนาดกระดานไม่ถูกต้อง")
        return

    # ขั้นตอนที่ 4: วนลูปหาพิกัดตำแหน่งของ King (ตัว 'K') บนกระดาน
    king_pos = None
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    # ขั้นตอนที่ 5: ถ้าวนหาจนจบแล้วไม่เจอ King ให้แจ้งเตือนและจบการทำงาน
    if not king_pos:
        print("ไม่พบKingในกระดาน")
        return
    
    # แยกพิกัดแถวและคอลัมน์ของ King เก็บไว้ใช้งาน
    kr, kc = king_pos

    # ขั้นตอนที่ 6: สร้างฟังก์ชันช่วยเช็คว่าพิกัดที่กำลังจะเดินไปตรวจ ยังอยู่ภายในขอบเขตกระดานจริงไหม
    def in_bounds(r, c):
        return 0 <= r < size and 0 <= c < size

    # ขั้นตอนที่ 7: ตรวจสอบเบี้ยฝ่ายตรงข้าม (Pawn - 'P') ที่อาจจะโจมตี King จากช่องเฉียงด้านหน้า
    for dc in (-1, 1):
        r = kr + 1
        c = kc + dc
        if in_bounds(r, c) and rows[r][c] == 'P':
            print("Success")
            return

    # กำหนดทิศทางการเดินของหมากแนวตรงและแนวทแยง
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # ขั้นตอนที่ 8: ตรวจสอบเรือ (Rook - 'R') และ ควีน (Queen - 'Q') ในแนวตรง 4 ทิศทาง
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            piece = rows[r][c]
            if piece != '.': # ถ้าเจอตัวหมากขวางอยู่
                if piece in ('R', 'Q'):
                    print("Success") # ถ้าเป็นเรือหรือควีน แปลว่าถูกรุก
                    return
                break # ถ้าเป็นหมากตัวอื่น ให้หยุดวิ่งในทิศทางนี้ (ถูกบล็อก)
            r += dr
            c += dc

    # ขั้นตอนที่ 9: ตรวจสอบบิชอป (Bishop - 'B') และ ควีน (Queen - 'Q') ในแนวทแยง 4 ทิศทาง
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            piece = rows[r][c]
            if piece != '.': # ถ้าเจอตัวหมากขวางอยู่
                if piece in ('B', 'Q'):
                    print("Success") # ถ้าเป็นบิชอปหรือควีน แปลว่าถูกรุก
                    return
                break # ถ้าเป็นหมากตัวอื่น ให้หยุดวิ่งในทิศทางนี้ (ถูกบล็อก)
            r += dr
            c += dc

    # ขั้นตอนที่ 10: ถ้าตรวจสอบทุกเงื่อนไขแล้วไม่มีการโจมตีโดน King เลย แสดงว่าปลอดภัย ให้พิมพ์ "Fail"
    print("Fail")