def calculator(sub1,sub2,sub3,sub4,sub5):
    total_marks = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total_marks / 500) * 100

    return total_marks, percentage

def grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80 and percentage < 90:
        return 'A'
    elif percentage >= 70 and percentage < 80:
        return 'B'
    elif percentage >= 60 and percentage < 70:
        return 'C'
    elif percentage >= 50 and percentage < 60:
        return 'D'
    else:
        return 'Fail'       