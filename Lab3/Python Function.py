import random
# Task 1


def in_ounces(n):
    return n / 28.3495231


"""
grams = float(input())
print(in_ounces(grams))
"""


# Task 2
def fahrenheit_to_celsius(n):
    return (5 / 9) * (n - 32)


"""
fahrenheits = float(input())
print(fahrenheit_to_celsius(fahrenheits))
"""


# Task 3
def solve(numheads, numlegs):
    for numRabbits in range(numheads + 1):
        numChickens = numheads - numRabbits
        if 2 * numChickens + 4 * numRabbits == numlegs:
            return numChickens, numRabbits


"""
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))
"""

# Task 4
"""
numbers = []
x = 5
for _ in range(x):
    y = int(input())
    numbers.append(y)
"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_prime(k):
    prime_numbers = []
    for n in k:
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers


# print(filter_prime(numbers))

# Task 5
def print_permutations(s):
    permutations = ['']

    for char in s:
        new_permutations = []

        for perm in permutations:

            for i in range(len(perm) + 1):
                new_permutations.append(perm[:i] + char + perm[i:])

        permutations = new_permutations

    for perm in set(permutations):
        print(perm)


"""
a = input()
print_permutations(a)
"""


# Task 6
def reverse_sentence(sentence):
    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = ""
    for word in reversed_words:
        if reversed_sentence:
            reversed_sentence += " " + word
        else:
            reversed_sentence = word
    return reversed_sentence


"""
a = input()
print(reverse_sentence(a))
"""


# Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


"""
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
"""


# Task 8
def spy_game(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == 0) and (nums[i + 1] == 0) and (nums[i + 2] == 7):
            return True
    return False


"""
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
"""


# Task 9
def volume(n):
    volumee = (4 * 3.14 * (n ** 2)) / 3
    return volumee


"""
radius = float(input())
print(volume(radius))
"""

# Task 10
p = [1, 2, 3, 4, 1, 3, 4]


def unique(n):
    o = []
    for item in n:
        if n.count(item) == 1:
            o.append(item)

    for item in o:
        print(item)


# unique(p)

# Task 11
def is_palindrome(s):
    return s == s[::-1]


# print(is_palindrome("madam"))

# Task 12
def histogram(a):
    for n in a:
        print('*' * n)


# histogram([4, 9, 7])

# Task 13



def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    cnt = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        cnt += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break


guess_the_number()

