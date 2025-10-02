"""

class StringKbtu:
    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

check = StringKbtu()
check.getString()
check.printString()
"""

"""

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
my_square = Square(7)
square_area = my_square.area()
print(f"The area of the square is: {square_area}")
"""

"""
class Shape:
    def area(self):
        return 0
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        
my_rectangle = Rectangle(5, 6)
rectangle_area = my_rectangle.area()
print(f"The area of rectangle is: {my_rectangle.area()}")
"""

"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()
p2.show()
print("Distance between p1 and p2:", p1.dist(p2))

"""

"""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

acc = Account("Alice", 100)

acc.deposit(50)
acc.deposit(200)

acc.withdraw(80)
acc.withdraw(500)   

"""

"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [2, 3, 4, 5, 10, 11, 15, 17, 20]

primes = list(filter(lambda x: is_prime(x), nums))

print("Prime numbers:", primes)


"""

