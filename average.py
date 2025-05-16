import csv
def calculate (score):
    #'''calculate the average of scores and round to 2 decimal place.'''
    return round(sum(score) / len(score),2)

def assign (avg):
    #Assigns a grade based on the average score using if-elif satatements.
    if avg >= 85:
        return"H"
    elif avg >= 75:
        return"X"
    elif avg >= 65:
        return"U"
    elif avg > 50:
        return"F"
    else:
        return"B"

"from utils import calculate average, assign grade"

def process_grades():
    studentgrades = []

#read student data from CSV
    with open("studentgrades.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) #Skip header row
        for row in reader:
            name,geography, chemistry, art = row
            score = list(map(int, [geography, chemistry, art])) #Covert score to integers
            total = sum(score)
            average = calculate(score)
            grade = assign(average)
            status = "Pass" if average >= 50 else "Fail"
            studentgrades.append((name, geography, chemistry, art, total, average, grade, status))
    return studentgrades

#Save processed data to a new CSV file
studentgrades = process_grades()

#Output to screen
for student in studentgrades:
    print(f"Name: {student[0]}, total: {student[4]}, average:{student[5]}, grade: {student[6]}, status: {student[7]}")

#Output to CVS
with open("studentgrades_results,csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'geography' , 'chemistry' ,'art', 'total', 'Average', 'Grade', 'status']) #Keep same column names
        writer.writerow(studentgrades)

        print("Results saved to student_results.csv")

# Simple division calculator with error handling
 
print("Welcome to the Division Calculator")
 
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print("Result:", result)
 
except ValueError:
    print("Error: Please enter only numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Thank you for using the calculator!")