# BMI_BMR_Calculator.py
# Splendid, 10/10 Code
# This program calculates the body mass index and basal metabolic rate

# Calculate BMI
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(m): '))

bmi = weight / height

print('BMI:  ', bmi)

# Calculate BMR
age = float(input('Enter age(years): '))
gender = input('Enter Gender(Male/Female): ').lower()

bmr = 0
if gender == "male":
    bmr =  10 * weight + 6.25 * (height * 100) - 5 * age + 5 # FIX: Multiply height by 100 for CM
else:
    bmr =  10 * weight + 6.25 * (height * 100) - 5 * age - 161 # FIX: Multiply height by 100 for CM
print('BMR: ', bmr)