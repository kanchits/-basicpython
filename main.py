# import ทั้งหมดทุกฟังก์ชันใน Module
#import number

#import มาบางฟังก์ชัน
#from number import factorial

# import และเปลี่ยนชื่อฟังชัน (นามแฝง) alias
from number import factorial as fa, fibonacci as fi
# เรียกใช้งาน import ไฟล์ number.py
# print(number.factorial(2))
# print(number.fibonacci(100))

print(fa(2))
print(fi(100))
