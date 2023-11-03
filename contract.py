contract = {'111':{'name':'Friend','job':'assassin','place':'America'},
            '112':{'name':'First','job':'warior','place':'German'},
            '113':{'name':'Finn','job':'magician','place':'Netherland' }}
contract['114'] = {'name':'Friren','job':'cook','place':'Frence' }

print('-----รหัสรายชื่อผู้ติดต่อ-----')

for i,c in enumerate(contract,start=1):
    print(f'{i} {c}')
while True:
    print('-----คุณต้องการติดต่อใคร-----')
    c = input('โปรดระบุรหัสรายชื่อติดต่อ: ')
    if c in contract:
        print(f'คนที่คุณต้องการติดต่อคือ {c} \nรายชื่อคือ {contract[c]['name']} \nอาชีพ {contract[c]['job']} \nสถานที่ทำงาน {contract[c]['place']} ')
    else:
        print('ไม่พบข้อมูลในระบบ')
    
    print('-----ขอบคุณสำหรับให้บริการ-----')


