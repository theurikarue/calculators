#Theuri Bonface Karue 
#SCT211-0573/2022

# BMI calculator

#Create A BMI Calculator app. After calculating the BMI of a person, the calculator should
# inform the person if they are underweight, Normal weight or Overweight. 


my_bmi = float(input("Enter your bmi: "))
#Defining normal bmi in my case normal bmi ranges from 18-26

normal_bmi_range = range (18,26)

if my_bmi == normal_bmi_range:
    print("You have normal weight ")
elif my_bmi < min(normal_bmi_range):
    print("You are  under-weight ")
elif my_bmi > max(normal_bmi_range):
    print("You are over-weight ")





 