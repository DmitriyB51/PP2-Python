# Task 1
class strings:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


"""
a = strings()
a.getString()
a.printString()
"""




#  Task 2 && 3
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)


"""
a = Square(100)
a.area()
"""


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


"""
b = Rectangle(5, 10)
b.area()
"""
# Task 4
import math


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)

    def move(self):
        self.x = int(input())
        self.y = int(input())

    def dist(self, other):
        print(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))


"""
a = point(10, 5)
b = point(3,4)
a.show()
a.move()
a.dist(b)
"""


# Task 5


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("IMPOSSIBLE")
        else:
            self.balance -= amount

    def currentbalance(self):
        print(self.balance)


"""
a = BankAccount("Dima", 0)
a.currentbalance()
a.deposit(1000)
a.currentbalance()
a.withdraw(500)
a.currentbalance()
a.withdraw(501) 
"""

# Task 6
numbers = []
x = 5
for _ in range(x):
    y = int(input())
    numbers.append(y)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# x = list(filter(lambda n: is_prime(n), numbers))
# print(x)
