import math
# ex 1
# deg = int(input())
def convert(deg):
    return math.radians(deg)
# a = convert(deg)
# print(a)

# ex 2
# height = int(input())
# base1 = int(input())
# base2 = int(input())
def area(height, base1, base2):
    return 0.5*(base1+base2)*height
# a = area(height,base1,base2)
# print(a)

# ex 3
# n = int(input())
# length = int(input())
def area2(n,length):
    return (n*length**2)/(4*math.tan(math.pi/n))
# a = area2(n,length)
# print(a)

# ex 4
l = int(input())
h = int(input())
def area3(l,n):
    return l*n
a = area3(l,h)
print(a)






















