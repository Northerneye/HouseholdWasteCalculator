import os
import csv
import numpy as np
import time
t = 0

age = []
fruits_vegetables = []
cereals = []
oilseeds_pulses = []
meats = []
fish_seafood = []
milk = []
other = []
people_per_income = []
age_calorie = []
average_calories_person = 2030.8

def get_data(filename): #loads the information from the csv file
    g = 0
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            g += 1
            if(g != 0 and g<=10):
                fruits_vegetables.append(float(row[12]))
                cereals.append(float(row[13]))
                oilseeds_pulses.append(float(row[14]))
                meats.append(float(row[15]))
                fish_seafood.append(float(row[16]))
                milk.append(float(row[17]))
                other.append(float(row[18]))
            if(g>28 and g<=37):
                people_per_income.append(float(row[4]))
            if(g>28 and g<=127):
                age_calorie.append(float(row[1]))
    return

def adjust_age(age):    #adjust the age to fit the index of the age_calorie array
    for i in range(len(age)):
        age[i] = age[i]-2
    return age

def adjust_income(income): #adjusts the income to fit one of eight brakets
    if(income<15000):
        return 0
    elif(income<30000):
        return 1
    elif(income<40000):
        return 2
    elif(income<50000):
        return 3
    elif(income<70000):
        return 4
    elif(income<100000):
        return 5
    elif(income<150000):
        return 6
    elif(income<200000):
        return 7
    else:
        return 8

def get_waste():    #runs the algorithm to find the food waste
    total_waste = 0
    for j in range(len(age)):   #runs the loop for each person in the family
        for i in range(7):  #finds the waste for each type of food
            if(i == 0):
                food_per_person = fruits_vegetables[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                fruits_vegetables_waste = food_per_person * calorie_ratio * fruits_vegetables[9]
            elif(i == 1):
                food_per_person = cereals[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                cereals_waste = food_per_person * calorie_ratio * cereals[9]
            elif(i == 2):
                food_per_person = oilseeds_pulses[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                oilseeds_pulses_waste = food_per_person * calorie_ratio * oilseeds_pulses[9]
            elif(i == 3):
                food_per_person = meats[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                meats_waste = food_per_person * calorie_ratio * meats[9]
            elif(i == 4):
                food_per_person = fish_seafood[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                fish_seafood_waste = food_per_person * calorie_ratio * fish_seafood[9]
            elif(i == 5):
                food_per_person = milk[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                milk_waste = food_per_person * calorie_ratio * milk[9]
            elif(i == 6):
                food_per_person = other[household_income]/people_per_income[household_income]
                calorie_ratio = age_calorie[int(age[j])]/average_calories_person
                other_waste = food_per_person * calorie_ratio * other[9]
        total_waste += fruits_vegetables_waste + cereals_waste + oilseeds_pulses_waste + meats_waste + fish_seafood_waste + milk_waste + other_waste    #adds the individuals waste to the total
    return total_waste

household_income = float(input("household income: "))   #prompts for household income
while(True):    #asks for the age of each family member
    os.system('cls')
    print("type 'finished' to compute")
    age_ = input("age of person "+str(t+1)+": ")
    if(age_ == "finished"):
        break
    age.append(float(age_))
    t += 1
household_income = adjust_income(household_income)
age = adjust_age(age)
get_data("food_income.csv") #loads data
household_waste = get_waste()   #runs the algorithm
os.system("cls")
print("household income: ",household_income)
print("family member ages ",age)
print(household_waste)  #outputs the total waste of the household
time.sleep(10)