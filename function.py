# การสร้างังก์ชันแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# สร้างฟังก์ชันแบบมีการ Return Value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังก์ชัน Helo()
hello("Kanchit.s")

# เรียกใช้งานฟังช์ area()
print(area(2, 5))
print("พื้นที่ทั้งหมด", area(15, 20))

# ฟังก์ชันแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="notdefine"):
    print(f"Name: {name}")
    print(f"salary: {name}")
    print(f"lang: {name}")


# เรียกใช้งานฟังก์ชัน show_info
show_info()
show_info('Kanchit.s', 50000, 'IT-Support')
