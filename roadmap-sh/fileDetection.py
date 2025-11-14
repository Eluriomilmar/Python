# Python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print(f"It is a file")

    else:
        print(f"It is not a file")
    if os.path.isdir(file_path):
        print("It is a directory")

    else:
        print("It is not a directory")

else:
    print(f"The location doesn't exist")