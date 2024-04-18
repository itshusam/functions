def average_grade(grades):
        
        total = sum(grades)
        average = total / len(grades)
        return average

def highest_and_lowest(grades):
    
        highest = max(grades)
        lowest = min(grades)
        return highest, lowest

def categorize(grades):
  
        letter_grades = []
        for grade in grades:
            if grade >= 85:
                letter_grades.append('A')
            elif grade >= 75:
                letter_grades.append('B')
            elif grade >= 65:
                letter_grades.append('C')
            elif grade >= 50:
                letter_grades.append('D')
            else:
                letter_grades.append('F')
        return letter_grades
