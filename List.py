number = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
name = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF']
mixed = [10, 20.20, True, 'Kanchit']

# การเข้าถึงสมาชิกใน list
print(number[9])
print(name[5])
print(mixed[1], mixed[3])

# การนับจำนวนสมาชิกใน list
print("สมาชิกทั้งหมดของ number =", len(number))

# การสร้าง list แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน list ว่าง
data.append(10)
data.append(20)
data.append(30)

print(data)

# การอัพเดทสมาชิกใน list
data[1] = 12

print(data)

# ฟังก์ชันวนลูปอ่านสมากชิกทั้งหมด
for n in number:
    print(n)


# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num
print(sum)
