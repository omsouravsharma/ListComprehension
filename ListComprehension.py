import pandas as pd

number = [1,1,2,3,4,8,13,21,34,55]

#  Exercise - 1
squared_number = [i**2 for i in number]
print(squared_number)
# Exercise - 2
even_number = [i for i in number if i % 2 == 0]
print(even_number)

file_1_list = []
file_2_list = []

with open("file1.txt") as file1:
    content_1 = file1.readlines()
    for i in content_1:
        int(i.strip())
        file_1_list.append(i)

with open("file2.txt") as file2:
    content_2 = file2.readlines()
    for i in content_2:
        int(i.strip())
        file_2_list.append(i)

print(file_1_list)
print(file_2_list)

new_list = [int(i) for i in file_1_list if i not in file_2_list]
print(new_list)

import random

student = ['sourav', 'gaurav', 'ram', 'shyam']

score_dic = {i: random.randint(1, 100) for i in student}
print(score_dic)

passed_student = {i:k for (i, k) in score_dic.items() if k > 50}
print(passed_student)

# Exercise

sentence = "What is airspeed velocity of a Unladen Swallow?"

list_words = sentence.split()
dict_comprehension = {
    i:len(i) for i in list_words
}

print(list_words)
print(dict_comprehension)

# Exercise

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
print(weather_c)
dict_comprehension = {i: ((k * 9/5)+32) for (i, k) in weather_c.items()}
print(dict_comprehension)

# Iterate Panda Dictionary:
import pandas as pd

student_dict = {
    "student": ['sourav', 'Gaurav', 'Hari'],
    "score": [56, 76, 98]
}

for (k, v) in student_dict.items():
    print(v)



student_df = pd.DataFrame(student_dict)
print(student_df)

for (k,v) in student_df.items():
    print(v)

# Loop through rows

for (index, row) in student_df.iterrows():
    print(row.student)

