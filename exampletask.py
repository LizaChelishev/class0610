_class = 0
while _class < 3:
    _class += 1
    print('Class is' , _class)
    i = 0
    _sum = 0
    while i < 5:
        grade = int(input('Please enter grade: '))
        if grade < 0 :
            break
        if grade == 0:
            i -= 1
            continue
        _sum += grade
        i += 1
    _avg = _sum / 5
    print('The average is' + str(_avg))
