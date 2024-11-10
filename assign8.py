
'''name = "Dhruvit"
print(f"Hello, {name}! Welcome!")'''

'''name = input("What is your name? ")
print(f"Hello, {name}! Welcome!")'''


'''import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")'''


'''length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")'''


'''num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_numbers = num1 + num2 + num3
product = num1 * num2 * num3
average = sum_numbers / 3
print(f"The sum of the numbers is: {sum_numbers}")
print(f"The product of the numbers is: {product}")
print(f"The average of the numbers is: {average}")
GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))
total_lots = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND) + (pounds * LOTS_PER_POUND) + lots
total_grams = total_lots * GRAMS_PER_LOT
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The equivalent weight is {kilograms} kilograms and {grams:.1f} grams.")'''

'''import random
lock_code_3_digit = [random.randint(0, 9) for _ in range(3)]
print("3-digit lock code:", ''.join(map(str, lock_code_3_digit)))
lock_code_4_digit = [random.randint(1, 6) for _ in range(4)]
print("4-digit lock code:", ''.join(map(str, lock_code_4_digit)))'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''import random
num_dice = int(input("How many dice would you like to roll? "))
total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1, 6) 
    total_sum += roll
print(f"The sum of the dice rolls is: {total_sum}")'''

'''numbers = []
while True:
    input_value = input("Enter a number (or press Enter to stop): ")
    if input_value == "":  
        break
    else:
        numbers.append(int(input_value))
numbers.sort(reverse=True)
top_five_numbers = numbers[:5]
print("The five greatest numbers are:", top_five_numbers)'''

'''number = int(input("Enter an integer: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")'''

'''cities = []

for i in range(5):
    city = input(f"Enter the name of city #{i+1}: ")
    cities.append(city)

print("The cities you entered are:")
for city in cities:
    print(city)'''

'''seasons = ("winter", "winter", "spring", "spring", "spring",
           "summer", "summer", "summer", "autumn", "autumn",
           "autumn", "winter")
month = int(input("Enter the number of the month (1-12): "))
if 1 <= month <= 12:
    season = seasons[month - 1]
    print(f"The season is: {season}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")'''


'''names = set()
while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "": 
        break
    elif name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("The names entered are:")
for name in names:
    print(name)'''

'''airports = {}

while True:
    choice = input("Choose an option: (1) Enter a new airport, (2) Fetch airport information, (3) Quit: ")

    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")
        airports[icao_code] = name
        print("Airport information saved.")

    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport: ").upper()
        if icao_code in airports:
            print(f"The airport name is: {airports[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")'''

'''number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1'''

'''conversion_factor = 2.54

while True:
    inches = float(input("Enter inches (negative value to quit): "))
    if inches < 0:
        break
    centimeters = inches * conversion_factor
    print(f"{inches} inches is {centimeters} centimeters")'''

'''numbers = []
while True:
    input_value = input("Enter a number (or press Enter to stop): ")
    if input_value == "":
        break
    numbers.append(float(input_value))
if numbers:
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
else:
    print("No numbers were entered.")'''

'''correct_username = "python"
correct_password = "rules"
attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password")
        attempts += 1
if attempts == 5:
    print("Access denied")'''


'''import random
points = int(input("Enter the number of random points to generate: "))
inside_circle = 0
for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1: 
        inside_circle += 1
approx_pi = 4 * (inside_circle / points)
print(f"Approximate value of pi: {approx_pi}")'''



