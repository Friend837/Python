# สร้างรายชื่อนักเรียน
students = []

# ฟังก์ชันเพิ่มนักเรียน
def add_student(name, score):
    student = {"ชื่อ": name, "คะแนน": score}
    students.append(student)

# ฟังก์ชันแสดงรายชื่อนักเรียน
def display_students():
    for student in students:
        print(f"ชื่อ: {student['ชื่อ']}, คะแนน: {student['คะแนน']}")

# ฟังก์ชันค้นหานักเรียน
def find_student(name):
    for student in students:
        if student["ชื่อ"] == name:
            print(f"พบนักเรียน: {student['ชื่อ']}, คะแนน: {student['คะแนน']}")
            return
    print(f"ไม่พบนักเรียนที่ชื่อ {name}")

# ฟังก์ชันลบนักเรียน
def delete_student(name):
    for student in students:
        if student["ชื่อ"] == name:
            students.remove(student)
            print(f"ลบนักเรียน: {name}")
            return
    print(f"ไม่พบนักเรียนที่ชื่อ {name}")

# ฟังก์ชันคำนวณคะแนนเฉลี่ย
def calculate_average_score():
    total_score = 0
    for student in students:
        total_score += student["คะแนน"]
    if len(students) > 0:
        average_score = total_score / len(students)
        print(f"คะแนนเฉลี่ย: {average_score}")
    else:
        print("ไม่มีนักเรียนในรายชื่อ")

# ฟังก์ชันแก้ไขคะแนนของนักเรียน
def edit_student_score(name, new_score):
    for student in students:
        if student["ชื่อ"] == name:
            student["คะแนน"] = new_score
            print(f"แก้ไขคะแนนของนักเรียน {name} เป็น {new_score}")
            return
    print(f"ไม่พบนักเรียนที่ชื่อ {name}")

# ตัวอย่างการใช้งาน
add_student("John", 85)
add_student("Alice", 92)
add_student("Bob", 78)

print("รายชื่อนักเรียน:")
display_students()

find_student("Alice")

delete_student("Bob")
print("รายชื่อนักเรียน หลังลบ:")
display_students()

calculate_average_score()

edit_student_score("John", 90)
print("รายชื่อนักเรียน หลังแก้ไขคะแนน:")
display_students()