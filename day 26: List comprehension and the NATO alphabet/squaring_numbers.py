import random
#squaring numbers
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [n**2 for n in numbers]

#filtering even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

#third exercise with comparing 2 txt files
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

#dictionary comprehension
#can create a new dictionary from values in list/dictionary
#new_dict = {new_key: new_value for item in list}

names = ["Amelia", "Sidney", "Jorge", "Ashley", "Vasiliki"]
student_scores = {student:random.randint(50,100) for student in names}

#pass if score is 60 or over
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}

