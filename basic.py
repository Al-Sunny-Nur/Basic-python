# # print('Hello world!')
# # print(3+4)
# # print('20',24)
# # print(type('Hello world!'))
# # print(type(4))
# # name=('Nur')
# # print(name)
# # num_1=12
# # num_2=8
# # print(num_1+num_2)
# # print(num_1-num_2)
# # print(num_1*num_2)
# # print(num_1/num_2)  
# # print(num_1//num_2)  # Floor division
# # print(num_1%num_2)  # Modulus
# # print(num_1**num_2)  # Exponentiation
# # print(num_1==num_2)  # Equality
# # print(num_1!=num_2)  # Not equal
# # print(num_1>num_2)  # Greater than
# # print(num_1<num_2)  # Less than
# # print(num_1>=num_2)  # Greater than or equal to
# # print(num_1<=num_2)  # Less than or equal to
# # print('Hello' + ' ' + 'World')  # String concatenation
# # print('Hello' * 3)  # String repetition
# # print('Hello' + str(3))  # Concatenating string with number
# # print('Hello' + str(3) + ' World')  # Concatenating string with number and another string

# # name='Nure'
# # Name='Nur'
# # print(name)
# # print(Name)
# # print(type(name))

# # a=15
# # b=6
# # print(a + b)  # Addition    
# # print(a - b)  # Subtraction
# # print(a * b)  # Multiplication
# # print(a / b)  # Division
# # print(a // b)  # Floor division
# # print(a % b)  # Modulus
# # print(a ** b)  # Exponentiation
# # print(a == b)  # Equality
# # print(a != b)  # Not equal
# # print(5>2)  # Greater than
# # print(5<2)  # Less than
# # print(2>=2)  # Greater than or equal to
# # print('Hello' + ' ' + 'World')  # String concatenation
# # print('Ramesh'in 'nure alam siddiq')  # Membership operator
# # print('Ramesh' not in 'nure alam siddiq')  # Membership operator

# # fruit = ['apple', 'banana', 'cherry']
# # print(fruit[0])  # Accessing the first element
# # print('banana' in fruit)  # Checking membership
# # print('orange' not in fruit)  # Checking non-membership
# # print(fruit[1:3])  # Slicing the list

# name=str (input('Enter your name: '))
# print(name)
# age=int(input('Enter your age: '))
# num_1=int(input('Enter first number: '))
# print(num_1)
# num_2=int(input('Enter second number: '))
# print('Sum:', num_1 + num_2)
# print('Difference:', num_1 - num_2)
# print(str(num_1) + ' + ' + str(num_2) + ' = ' + str(num_1 + num_2))
# print(str(20) + '24')
# print('Hello ' + name + ', you are ' + str(age) + ' years old.')

# # if this:
# #     do something

# # else:
# #     do something else

# if num_1 > num_2:
#     print('First number is greater than second number.')
# else:
#     print('First number is not greater than second number.')

# num_3 = int(input('Enter a number: '))
# if num_3 % 2 == 0:
#     print('The number is even.')    
# else:
#     print('The number is odd.')

# temperature = float(input('Enter temperature in Celsius: '))
# if temperature < 0:
#     print('It is freezing outside.')
# elif temperature >= 0 and temperature <= 30:
#     print('The weather is pleasant.')
# elif temperature > 30 and temperature <= 40:
#     print('It is warm outside.')

# n=int(input('Enter a number: '))
# if  n%3== 0 and n%5==0:
#     print('FizzBuzz')
# elif n%3==0:
#     print('Fizz')
# elif n%5==0:
#     print('Buzz')
# else:
#     print('Not a FizzBuzz number')
# # Using a for loop to iterate through a range of numbers

# if 5%2 == 0:
#     print('5 is even')  
# else:
#     print('5 is odd')

# list_of_numbers1 = [1, 2, 3, 4, 5]
# list_of_numbers2 = [6, 7, 8, 9, 10]
# # Using a for loop to iterate through a list
# new_list = list_of_numbers1 + list_of_numbers2  # Concatenating two lists
# for number in new_list:
#     print(number)  # Printing each number in the list
# list_of_numbers1.append(6)  # Adding an element to the list
# print('List of numbers1:', list_of_numbers1)
# print('First number:', list_of_numbers1[-1]) # Accessing the last element

# student = {
#     'name': 'Nure',
#     'age': 20,
#     'subjects': ['Math', 'Science', 'English']
# }

# student['age'] = '27'  # Updating the name
# print('Student Name:', student['name'])  # Accessing the name   
# print('Student Age:', student['age'])  # Accessing the age
# print('Student Subjects:', student['subjects'])  # Accessing the subjects
# print('Student', student)  # Printing the entire dictionary

# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     if fruit == 'banana':
#         print('Found a banana!')  # Checking for a specific fruit
#     else:       
#         print('This is not a banana.')
#     print(fruit)  # Printing each fruit in the list 

# for i in range(5):
#     print(i)  # Printing numbers from 0 to 4
# for raysha in range(5, 10):
#     print(raysha)  # Printing numbers from 5 to 9

# count = 0
# while count < 100:
#     # Printing numbers from 0 to 4
#     count += 1  # Incrementing the count by 1   
#     print('Love you Babeeeee')  # Indicating the end of the loop

# fruits = ('apple', 'banana', 'cherry')
# print(fruits[0])  # Accessing the first element
# fruits[0]= 'orange'  # Attempting to change the first element (will raise an error)
# print(fruits) # fruits.append('kiwi')  # Attempting to append an element (will raise an error)

fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Accessing the first element
fruits[0] = 'orange'  # Changing the first element
print(fruits)  # Printing the updated list
fruits.append('kiwi')  # Appending an element
fruits.append('mango')  # Appending another element
print(fruits)  # Printing the list after appending
fruits.remove('banana')  # Removing an element
print(fruits)  # Printing the list after removing an element
fruits.pop()  # Removing the last element   
print(fruits)  # Printing the list after popping the last element
fruits.clear()  # Clearing the list
print(fruits)  # Printing the empty list after clearing
fruits.sort()  # Sorting the list (will raise an error since the list is empty)
print(fruits)  # Printing the sorted list (will raise an error since the list is empty)
fruits.reverse() # Reversing the list (will raise an error since the list is empty)
print(fruits)  # Printing the reversed list (will raise an error since the list is empty)

for index, fruit in enumerate(fruits) :
    print(index, fruit)  # Printing each fruit in the list (will not execute since the list is empty)

# my_numbers = [1, 2, 3, 2, 3, 4, 5]
# print(my_numbers)  # Printing the list of numbers
# my_numbers.append(6)  # Appending a number to the list
# print(my_numbers)  # Printing the list after appending
# my_numbers.remove(2)  # Removing the first occurrence of 2 from the list
# print(my_numbers)  # Printing the list after removing 2
# my_numbers.sort()  # Sorting the list
# print(my_numbers)  # Printing the sorted list
# my_numbers.reverse()  # Reversing the list
# print(my_numbers)  # Printing the reversed list

# my_numbers.clear()  # Clearing the list
# print(my_numbers)  # Printing the empty list after clearing

# students = [
#     {'name': 'Alice', 'age': 20},
# ]

# print(students)  # Printing the list of students
# students.append({'name': 'Bob', 'age': 22})  # Appending a new student
# print(students)  # Printing the list after appending a new student

# a = 5
# b = 7
# def sum(a, b):
#     return a + b  # Function to calculate the sum of two numbers    
# result = sum(a, b)  # Calling the function with a and b
# print('Sum:', result)  # Printing the result of the sum function
# def greet(name):
#     return 'Hello, ' + name + '!'  # Function to greet a person by name 

add = lambda x, y: x + y  # Lambda function to add two numbers
print('Sum using lambda:', add(5, 7))  # Printing the result of the lambda function

for i in range(10):
    print('I LOVE YOU')  # Printing "Hello, World!" five times

from datetime import datetime as dt
print('Current date and time:', dt.now())  # Printing the current date and time
print('Current year:', dt.now().year)  # Printing the current year
print('Current month:', dt.now().month)  # Printing the current month   
print('Current day:', dt.now().day)  # Printing the current day
print('Current hour:', dt.now().hour)  # Printing the current hour
print('Current minute:', dt.now().minute)  # Printing the current minute
print('Current second:', dt.now().second)  # Printing the current second

def check_log_for_errors_with_for(log_file):
   
   try: 
         with open(log_file, 'r') as file:
              print('Checking log file for errors...')
              for line_number,line in enumerate (log_file):
                  if 'ERROR' in line:
                       print('Error found:', line.strip())

        
   except FileNotFoundError:
        print('Log file not found:', log_file)
   except Exception as e:
        print('An error occurred:', str(e))
# Function to check log file for errors using a for loop
path = './logfile.log'
check_log_for_errors_with_forlog_File_name = './logfile.log'