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
'''import numpy as np
from contourpy.util import data
from matplotlib import pyplot as plt'''

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


'''class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        # Add the edge from u to v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

        # Since the graph is undirected, add edge from v to u as well
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# Creating the graph
g = Graph()

# Adding the edges as per the graph
g.add_edge('A', 'B', 76)
g.add_edge('A', 'C', 47)
g.add_edge('A', 'E', 47)
g.add_edge('B', 'C', 47)
g.add_edge('B', 'D', 49)
g.add_edge('C', 'D', 54)
g.add_edge('C', 'E', 47)

# Printing the graph
g.print_graph()'''

'''import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("linreg_data.csv",skiprows=0,names=["x","y"])
print(data)
A = np.arry([1,2,3],[4,5,6])
np.sum(A)
np.sum(A,0)
np.sum(A,1)
np.prod(A)
np.prod(A,0)
np.prod(A,1)
np.min(A)
np.min(A,0)
np.min(A,1)
np.max(A)
np.max(A,0)
np.max(A,1)
np.mean(A)
np.mean(A,0)
np.mean(A,1)
np.median (A)
np.median(A,0)
np.median(A,1)
np.std(A)
np.std(A,0)
np.std(A,1)
np.var(A)
np.var(A,0)
np.var(A,1)
xpd = data["x"]
ypd = data["y"]
n = xpd.size
plt.scater(xpd,ypd)
plt.show()
xbar = np.scam(xpd)
ybar = np.scam(ypd)
term1 = np.sum(xpd)
term2 = np.sum(ypd)
term1 = np.sum(xpd*ypd)
b = (term1-n*xbar*ybar)/(term2-n*xbar*xbar)
a = ybar - b*xbar
x = np.linspace(0,2,100)
y = a+b*x
plt.plot(x,y,colour="black")
plt.scatter(xpd,ypd)
plt.scatter(xbar,ybar,colour="red")
plt.show()'''

'''import numpy as np
from sklearn import linear_model
my_data = np.genfromtxt("linreg_data.csv",delimiter=",")
xp = my_data[:,0]
yp = my_data[:,1]
xp = xp.reshape(-1,1)
yp = yp.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(xp,yp)
print(regr.coef_,regr.intercept_)
xval = np.full ((1,1),0.5)
yval = regr.predict(xval)
print(yval)
xval = np.linspace (-1,2,20).reshape(-1,1)
yval = regr.predict(xval)
plt.plot(xval,yval)
plt.scatter(xp,yp,color='red')
plt.show()
from sklearn import metrics
yhat = regr.predict(xp)
print('Mean Absolute error: ', metrics.mean_absolute_error(yp,yhat))
print('Mean Squared error: ', metrics.mean_squared_error(yp,yhat))
print('Root mean squared error: ', metrics.root_mean_squared_error(yp,yhat))
print('R2 value: ', metrics.r2_score(yp,yhat))'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data_pd = pd.read_csv("quadreg_data.csv",skiprows=0,names=["x","y"])
print(data_pd)

xpd = np.array(data_pd["x"])
ypd = np.array(data_pd["y"])
xpd = xpd.reshape(-1,1)
ypd = ypd.reshape(-1,1)
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(xpd)
pol_reg = LinearRegression()
pol_reg.fit(X_poly,ypd)
plt.scatter(xpd,ypd, color='red')
xval = np.linspace(-1,1,10).reshape(-1,1)
plt.plot(xval,pol_reg.predict(poly_reg.transform(xval)), color="blue")
plt.show()
print(pol_reg.coef_)
print("c=",pol_reg.intercept_)


