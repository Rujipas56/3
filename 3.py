# กำหนดเซต a และ b
a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}

# 1. Union (ผลรวมของสมาชิกทั้งหมดใน a และ b)
result_union = a | b
print("ผลลัพธ์ของ a | b =", result_union)

# 2. Intersection (ค่าที่มีในทั้ง a และ b)
result_intersection = a & b
print("ผลลัพธ์ของ a & b =", result_intersection)

# 3. Difference (ค่าที่มีใน a แต่ไม่มีใน b)
result_difference = a - b
print("ผลลัพธ์ของ a - b =", result_difference)

# 4. Symmetric Difference (ค่าที่ไม่ซ้ำกันใน a และ b)
result_sym_diff = a ^ b
print("ผลลัพธ์ของ a ^ b =", result_sym_diff)
