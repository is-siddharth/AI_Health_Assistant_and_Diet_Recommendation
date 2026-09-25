def bmi_calculator(weight, height): # Body Mass Index
    bmi = weight / ((height/100)**2) # weight must be in kg and height in m (Conversion)
    return round(bmi,2)

def bmr_calculator(weight, height, age, gender): # Basal Metabolic Rate (Diff. for Male & Female)
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        return bmr
    elif gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        return bmr

def tdee_calculator(bmr, activity): # Total Daily Energy Expenditure (Activity Factor --> Some other factors)
    #Define all the factors
    activity_factor = {
        "Sedentary": 1.20, 
        "Lightly_Active": 1.375, 
        "Moderately_Active": 1.55, 
        "Very_Active": 1.725, 
        "Extra_Active": 1.90
    }
    tdee = bmr * activity_factor[activity]
    return round(tdee,2)

def calorie_target(tdee, aim):
    if aim == "weight maintain":
        calorie = tdee
    elif aim == "weight loss":
        calorie = tdee - 400
    elif aim == "weight gain": 
        calorie = tdee + 300
    return calorie

# print(bmi_calculator(90, 180))
# print(bmr_calculator(90, 170, 24, "male"))
# bmr = bmr_calculator(90, 170, 24, "male")
# print(tdee_calculator(bmr, "Moderately_Active"))
# tdee = tdee_calculator(bmr, "Moderately_Active")
# print("Your Final T")
# print(calorie_target(tdee, "weight loss"))
