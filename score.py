score = [7,9,5,1,5,6,7,8,9,5,7,5]
score.append(10)
score.insert(0,3)
score.remove(3)
score.pop(0)
for i,c in enumerate(score,start = 1):
    print(f'ลำดับที่ {i},ได้คะแนน {c}')
    