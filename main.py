import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")
file_nato = pd.DataFrame(file)
print(file_nato)


dict_nato = {
    row.letter: row.code for (index, row) in file_nato.iterrows()
}
print(dict_nato)
is_on = True
while is_on:
    try:
        user_input = input("Please enter your name: ").upper()
        list_comprehension = [dict_nato[i] for i in user_input]

    except KeyError:
        print("Sorry, Only Letter in the alphabet please")
    else:
        print(list_comprehension)
        is_on = False
