#print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal='Bang energy drink'

#print('1.2: Print the meal variable')
print(meal)

#print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal='pot roast'
print(meal)

# print('2: How old is Google?')
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year
current_year=2022
year_founded=1993
google_age=current_year-year_founded

# 2.2: Print out a sentence about Google's age. Make sure to include your variable in the f-string!
print(f'Google is {google_age} years old')


# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print the info.
# (Assume 12 months for each year, you don't need to check which month they started)
google_age_months=google_age*12
print(f'Google is {google_age_months} months old')


print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
print('Fix the problem and turn the comment back into regular Python code')
completion_message = 'Completed the first Python challenge!'

# 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
print('There was a space in the variable name that needed to be replaced with a _')
print('There was also no quotation mark at the end of the print statement so I added one')
print('3.3: Turn the comment below back into regular Python code')
print(completion_message)
