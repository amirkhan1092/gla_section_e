# customer requirements
total_amount = int(input('enter the total amount '))

# seller storage
bar_1kg = int(input('enter the number of bar of 1kg '))
bar_5kg = int(input('enter the number of bar of 5kg'))
bar_use_5kg = 0
bar_use_1kg = 0
if total_amount >= 5:
    bt5 = (total_amount//5)-bar_5kg
    if bt5 >= 0:
        # print('5kg bar used with amount of ', bar_5kg)
        bar_use_5kg = bar_5kg
        total_amount -=(bar_use_5kg*5)
    else:
        bar_use_5kg = bar_5kg-abs(bt5)
        total_amount -=(bar_use_5kg*5)
        # print('5kg bar used with amount of : ', bar_temp)

while total_amount > 0 and bar_1kg >0:
    total_amount -= 1
    bar_use_1kg += 1
    bar_1kg -= 1
if total_amount > 0:
    print('the material is short try again ')
else:
    print('5kg bar used with amount of : ', bar_use_5kg)
    print('1kg bar used with amount of : ', bar_use_1kg)