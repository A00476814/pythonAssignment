import pandas as pd

def count_No_Of_Vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in str(string) if char in vowels)

def count_vowels_in_csv(file_name, column_name):
    df = pd.read_csv(file_name)


    df['noOfVowels'] = df[column_name].apply(count_No_Of_Vowels)

    df.to_csv("output.csv", index=False)
    
    

# Please enter your file name as first parameter to load data in DF and the column name as second parameter.
count_vowels_in_csv('titles.csv', 'title')


