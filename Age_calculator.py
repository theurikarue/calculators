#Theuri Bonface Karue 
#SCT211-0573/2022


#Age calculator 


from datetime import datetime

#define function for calculating age
def calculate_age(birthday):
    birthdate = datetime.strptime(birthday, "%Y-%m-%d")
    current_date = datetime.now()

    age = current_date - birthdate
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    return years, months, days


birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
years, months, days = calculate_age(birthdate)




print(f"Your age is {years} years, {months} months, and {days} days.")




