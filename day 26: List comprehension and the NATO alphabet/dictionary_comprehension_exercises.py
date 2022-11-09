#exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#convert a string into a list of words
sentences = sentence.split()

#create comprehension
result1 = {word:len(word) for word in sentences}
print(result1)

#exercise 2: convert dictionary of temperatures in celcius to farenheight
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}

#iterate over a pandas data frame
student_dict = {
    "student": ["Amelia", "Tanya", "Michelle"],
    "score": [90, 80, 70]
}
#looping through dictionaries
for (key, value) in student_dict.items():
    print(key)

#loop through data frame
import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

#loop through rows of data frame
for (index, row) in student_df.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Amelia":
        print(f"Amelia's score is {row.score}")