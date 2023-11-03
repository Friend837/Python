def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

while True:
    print('--------โปรแกรมคำนวณเกรด--------')
    score = int(input('กรุณาใส่คะแนนของคุณ: '))
    name = input('กรุณาระบุชื่อของคุณ: ')
    print(f"ชื่อของคุณคือ: {name} คะแนน {score} ได้เกรด: {grade(score)}")
    print('--------จบการคำนวณ--------')






