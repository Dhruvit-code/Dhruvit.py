'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def print_properties(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

new_car = Car("ABC-123", 142)

new_car.print_properties()'''


'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change


        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def print_properties(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Current Speed after accelerations: {new_car.current_speed} km/h")'''


'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

       
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):

        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

    def print_properties(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance:.2f} km")


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Current Speed after accelerations: {new_car.current_speed} km/h")

new_car.drive(1.5)

print(f"Travelled Distance after 1.5 hours of driving: {new_car.travelled_distance:.2f} km")

new_car.accelerate(-200)

print(f"Final Speed after emergency brake: {new_car.current_speed} km/h")'''

'''import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):

        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

    def print_properties(self):
        print(
            f"{self.registration_number:<10} | {self.max_speed:>11} km/h | {self.current_speed:>13} km/h | {self.travelled_distance:>17.2f} km")



cars = [Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]


race_ongoing = True
hours_passed = 0

while race_ongoing:
    hours_passed += 1
    print(f"--- Hour {hours_passed} ---")

    for car in cars:

        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)


        car.drive(1)


        if car.travelled_distance >= 10000:
            race_ongoing = False


    print("Registration | Max Speed    | Current Speed | Travelled Distance")
    print("-------------------------------------------------------------")
    for car in cars:
        car.print_properties()
    print()


print("The race has ended! Final standings:")
print("Registration | Max Speed    | Current Speed | Travelled Distance")
print("-------------------------------------------------------------")
for car in cars:
    car.print_properties()'''


'''class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    pass


class NegativeAmountException(Exception):
    """Custom exception for negative amounts."""
    pass


def withdraw_money():
    try:
        
        balance = float(input("Enter your account balance: "))
        if balance < 0:
            raise NegativeAmountException("The account balance cannot be negative.")


        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        if withdrawal_amount < 0:
            raise NegativeAmountException("The withdrawal amount cannot be negative.")


        if withdrawal_amount > balance:
            raise InsufficientFundsException("The withdrawal amount exceeds the current balance.")


        balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")

    except ValueError:

        print("Invalid input! Please enter numeric values only.")

    except NegativeAmountException as e:

        print(f"Error: {e}")

    except InsufficientFundsException as e:

        print(f"Error: {e}")



withdraw_money()'''



'''def write_notes(filename):
    """Write new notes to the file, overwriting any existing content."""
    notes = input("Enter your notes (these will overwrite any existing content): ")
    with open(filename, 'w') as file:
        file.write(notes + '\n')
    print("Notes written to the file successfully.")

def read_notes(filename):
    """Read and display the notes from the file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if content:
                print("\n--- Your Notes ---")
                print(content)
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("No notes found. The file does not exist.")

def append_notes(filename):
    """Append new notes to the file without removing existing content."""
    additional_notes = input("Enter additional notes to append: ")
    with open(filename, 'a') as file:
        file.write(additional_notes + '\n')
    print("Notes appended to the file successfully.")

def main():
    filename = "notes.txt"

    while True:
        print("\nChoose an option:")
        print("1. Write new notes (overwrites existing content)")
        print("2. Read existing notes")
        print'''



