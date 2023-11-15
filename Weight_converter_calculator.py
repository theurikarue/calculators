'''num_1 = input("Enter 1st number: ")
num_2 = input("Enter 2nd number: ")

sum = int(num_1) + int(num_2)


print("The sum of two numbers is: " + str(sum))



'''
'''course = "Computer science "
print(course.isupper())'''


'''x = 3>1
print(x)'''

#weight converted calculator
def weight_converter():
    try:
        weight = float(input("Enter weight: "))
        units = input("Is this weight in k (kilograms) or l (pounds)? ").lower()

        if units == "l":
            converted_weight = weight / 2.2
            print(f"Your weight in kilograms is: {converted_weight:.2f} kg")
        elif units == "k":
            converted_weight = weight * 2.2
            print(f"Your weight in pounds is: {converted_weight:.2f} lbs")
        else:
            print("Invalid unit. Please enter 'k' or 'l' for kilograms or pounds.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric weight.")

# Call the function to execute the weight converter
weight_converter()
