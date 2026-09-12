sub = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Hindi', 'English', 'SST', 'AI']
marks = []

for i in sub:
    while True:
        try:
            user = input(f'Enter your marks in {i} or "s" to skip: ').lower().strip()
            if user == 's':
                break

            elif float(user) < 0 or float(user) > 100:
                print('invalid')

            else:
                f = float(user)
                marks.append(f)
                break
        except ValueError:
            print('Invalid input')

total = sum(marks)
x = len(marks)
if x > 0:
    percentage = (total / (x * 100)) * 100
    if percentage >= 90:
        Grade = 'A'
    elif 90 > percentage >= 75:
        Grade = 'B'
    elif 75 > percentage >= 55:
        Grade = 'C'
    else:
        Grade = 'Need Improvement'

    print(f'total marks: {total}')
    print(f'percentage: {percentage}')
    print(f'Grade: {Grade}')
else:
    print('No marks Recorded')





          
          