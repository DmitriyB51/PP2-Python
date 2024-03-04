import os

# ex 1
path = r"C:\Users\OmeN_HP\PycharmProjects\PP2 PYTHON"


# only directories

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


# only files

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


# files and directories

def list_dirs_and_files(path):
    dirs = list_directories(path)
    files = list_files(path)
    return dirs, files


# print("Directories:", list_directories(path))
# print("Files:", list_files(path))
# print("Directories and Files:", list_dirs_and_files(path))

# ex 2
def existance(path):
    exist = os.path.exists(path)
    if exist:
        print("Path exists")

        readable = os.access(path, os.R_OK)
        if readable:
            print("Path is readable")
        else:
            print("Path is NOT readable")

        writable = os.access(path, os.W_OK)
        if writable:
            print("Path is writable")
        else:
            print("Path is NOT writable")

        executable = os.access(path, os.X_OK)
        if executable:
            print("path is executable")
        else:
            print("Path is NOT executable")

    else:
        print("Path is NOT exists")
# existance(path)

# ex 3
def check(path):

    if os.path.exists(path):
        print("Path exists")
        # Extract and print directory name
        directory_name = os.path.dirname(path)
        print(f"Directory: {directory_name}")
        # Extract and print file name
        file_name = os.path.basename(path)
        print(f"Filename: {file_name}")
    else:
        print("Path is NOT exists")
# check(path)

# ex 4
# path = r"C:\Users\OmeN_HP\PycharmProjects\PP2 PYTHON\practice\1.py"
def counter(path):
    cnt = 0
    with open(path, 'r') as file:
        for line in file:
            cnt+=1

    print(cnt)

# counter(path)

# ex 5
# path = r"C:\Users\OmeN_HP\PycharmProjects\PP2 PYTHON\practice\1.py"
def append(path, my_list):

    with open(path, 'a') as file:
        file.write(str(my_list))

my_list = ['a','b','c']
# append(path, my_list)

# ex 6
def generate_alphabet_files():
    for i in range(65, 91):  # ASCII values for A-Z
        filename = f"{chr(i)}.txt"

# generate_alphabet_files()

# ex 7
path1 = r"C:\Users\OmeN_HP\PycharmProjects\PP2 PYTHON\practice\1.py"
path2 = r"C:\Users\OmeN_HP\PycharmProjects\PP2 PYTHON\practice\4.py"
def transfer(path1, path2):
    with open(path1, 'r') as file1:
        with open(path2, 'w') as file2:
            content = file1.read()
            file2.write(content)

transfer(path1, path2)

# ex 8
def delete(path2):
    if os.access(path2, os.W_OK):
        if os.path.exists(path2):
            os.remove(path2)
# delete(path2)