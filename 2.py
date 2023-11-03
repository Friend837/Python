def grade():
    score = int(input('กรุณาใส่คะแนนของคุณ: '))
    name = input('กรุณาระบุชื่อของคุณ: ')
    while True:
        print(f"ชื่อของคุณคือ: {name} คะแนน {score} ได้เกรด {grade}")
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
