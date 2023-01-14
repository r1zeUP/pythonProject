import os

directory = "inner"
os.mkdir(directory)

filename = "1.txt"

path = os.path.join(directory, filename)

with open(path, "w", encoding='utf-8') as file:
    file.write("")

file_exists = os.path.exists(path)

print(file_exists)
