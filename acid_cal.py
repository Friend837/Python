print('-----โปรแกรมคำนวณการแตกตัวของยา 2 ตัวโดยใช้ pka-----')
acidt = {'acid':1,'base':-1}

try:
    acid_1 = input('ยาตัวที่ 1 เป็นกรดหรือเบส [acid / base]: ')
    drug_1 = float(input('ระบุค่า pKa ของยาตัวที่ 1: '))
    acid_2 = input('ยาตัวที่ 2 เป็นกรดหรือเบส [acid / base]: ')
    drug_2 = float(input('ระบุค่า pKa ของยาตัวที่ 2: '))
    pH = float(input('ระบุค่า pH ของ condition: '))
except:
    print('กรุณาระบุเป็นตัวเลขทศนิยม')
    acid_1 = input('ยาตัวที่ 1 เป็นกรดหรือเบส [acid / base]: ')
    drug_1 = int(input('ระบุค่า pKa ของยาตัวที่ 1: '))
    acid_2 = input('ยาตัวที่ 2 เป็นกรดหรือเบส [acid / base]: ')
    drug_2 = int(input('ระบุค่า pKa ของยาตัวที่ 2: '))
    pH = float(input('ระบุค่า pH ของ condition: '))

salt_01 = acidt[acid_1] * (pH - (drug_1))
salt_1 = 10 ** salt_01
salt_02 = acidt[acid_2] * (pH - (drug_2))
salt_2 = 10 ** salt_02
dis_1 = 100 * salt_1/(1 + salt_1)
dis_2 = 100 * salt_2/(1 + salt_2)
#pH=pka+log(เกลือ/กรด,10), salt/(100-salt)=ph, salt+ph*salt=100ph,salt=100ph/(1+ph)


print('------คำนวณ-----')
print(f'[เกลือ]/[กรด] ของยาตัวที่ 1 = {salt_1}')
print(f'ยาตัวที่ 1 แตกตัวได้ = {dis_1}%')
print(f'[เกลือ]/[กรด] ของยาตัวที่ 2 = {salt_2}')
print(f'ยาตัวที่ 2 แตกตัวได้ = {dis_2}%')
