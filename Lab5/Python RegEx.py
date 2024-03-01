import re

# ex 1
# text = str(input())
def match(text):
    pattern = 'ab*'
    if re.match(pattern, text):
        print('Match')
    else:
        print('Not matched')
# match(text)


# ex 2
# text = str(input())
def match1(text):
    pattern = 'ab{2,3}'
    if re.match(pattern, text):
        print('Match')
    else:
        print('Not matched')
# match1(text)

# ex 3
# text = str(input())
def seq(text):
    pattern = '[a-z]+_[a-z]+'
    a = re.findall(pattern, text)
    return a
# b = seq(text)
# print(b)

# ex 4
# text = str(input())
def seq1(text):
    pattern = '[A-Z][a-z]+'
    a = re.findall(pattern,text)
    print(a)
# seq1(text)

# ex 5
# text = str(input())
def match2(text):
    pattern = 'a.*b$'
    a = re.search(pattern,text)
    if(a):
        print('Match!')
    else:
        print('Not matched!')
# match2(text)

# ex 6
# text = str(input())
def replace(text):
    pattern = '[ ,.]'
    a = re.sub(pattern,":" , text)
    print(a)
# replace(text)

# ex 7
# text = str(input())
def snake_to_camel(text):

    words = text.split('_')

    a = words[0] + ''.join(i.capitalize() for i in words[1:])
    print(a)
# snake_to_camel(text)

# ex 8
# text = str(input())
def spl(text):
    pattern = '[A-Z][^A-Z]*'
    a = re.findall(pattern, text)
    print(a)
# spl(text)

# ex 9
# text = str(input())
def space(text):
    a = spaced_text = re.sub(r"(\B[A-Z])", r" \1", text)
    print(a)
# space(text)

# ex 10
text = str(input())
def camel(text):
    a = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    print(a)
camel(text)





