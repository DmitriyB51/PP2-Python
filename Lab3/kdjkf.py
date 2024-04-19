"""
# Task 1
s = str(input())
s = s[::-1]
d = ""

for i in range(len(s)):
    if i % 2 == 1:
        d += s[i]

print(d)

"""
# Task 2
x = int(input())
y = int(input())  #
def a(x,y):
    for i in range(0,3):
        if x != i:
            print(3*"*")
        elif y == 0:
            print("0" + "*" + "*")
        elif y == 1:
            print("*" + "0" + "*")
        elif y == 2:
            print("*" + "*" + "0")
            



a(x,y)





