def letterGrade():
    arrScores = []
    arrGrades = []
    while (len(arrScores) < 10):
        print
        score = input('Enter a score between 60 and 100: ')

        if (score < 60 or score > 100):
            score = input('Score must be between 60 and 100. Try again: ')

        if (score <= 100 and score >= 90):
            grade = 'A'
        elif (score <= 89 and score >= 80):
            grade = 'B'
        elif (score <= 79 and score >= 70):
            grade = 'C'
        elif (score <= 69 and score >= 60):
            grade = 'D'
        arrScores.append(score)
        arrGrades.append(grade)

    print ('Score and Grades')
    for i in range(0,10):
        print ('Score: {}; Your grade is {}'.format(arrScores[i],arrGrades[i]))
    print ('End of the program. Bye!')

letterGrade()
