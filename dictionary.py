scores = {
    'AAA': 1000,
    'BBB': 2000,
    'CCC': 3000
}

print(scores)
print(scores['AAA'])

# เพิ่มสามาชิกใหม่เข้า dictionary
scores['CCC'] = 3000

print(scores)

# การสร้าง dictionary ว่าง
points = {}

# เพิ่มต่าเข้า dictionary ว่าง
points['mr_a'] = 10.2
points['mr_a'] = 10.2
points['mr_a'] = 10.2

print(points)

# การ loop อ่านสมาชิกของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)
