# Spiltwise calculator
print("Welcome to the spiltwise App")
total_bill = input("what was the total bill? $")
total_bill = float(total_bill)
tip = input("how much tip would you like to give? 10% 12% or 15%")
tip = float(tip)
People = input("How many people spilt the bill?")
People = int(People)
add_tip_in_total_bill = total_bill * (tip/100)
new_bill = total_bill + add_tip_in_total_bill
each_person_pay = new_bill / People
print(f"Each person should pay: {round(each_person_pay,2)}")



#(2) How many week left in human life count
# age = input()
# years = 90 - int(age)
# weeks = years * 52
# print(f"you have {weeks} left")



#(3) BMI calculator
# print("enter your height in centimeters:")
# height = input()
# print("enter your weight in kilograms:")
# weight = input()
# height = float(height)
# weight = float(weight)
# bmi = weight / (height * height)
# print("your body mask index is " + str(bmi))
# print(f"your body mask index is {bmi})