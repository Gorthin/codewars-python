'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5 : return "Underweight"
    elif bmi <= 25 : return "Normal"
    elif bmi <= 30 : return "Overweight"
    else: return "Obese"