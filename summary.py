print("-----------------------------------")
print(" #Summation Program")
print(" # Type 'exit' to end ther program")
print("-----------------------------------")

# ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1
while True:
    data = input(f"Enter Number {count}:")
    # ตรวจว่าผู้ใช้ป้อน 'Exit'
    if data == 'exit':
        break
    # การหาผลรวม
    sumdata += int(data)
    cout = count+1

print(f"Sum value is {sumdata}")
