import re

pattern = r'(\d+?\ [a-z]|[a-z]+|[A-Z]|^\#)'
spaces_pattern = r'\ {2,3}'

input_file = open("x19.txt", "r")

arr_of_lines = input_file.readlines()

input_file.close()
arr_of_data = []

for line in arr_of_lines:
    if not re.match(pattern, line):
        arr_of_data.append(line)

for index in range(0, len(arr_of_data)):
    arr_of_data[index] = re.sub(spaces_pattern, ";", arr_of_data[index])
    arr_of_data[index] = re.sub(r'\.', ',', arr_of_data[index])

output_file = open("output.csv", "w")

for line in arr_of_data:
    output_file.write(line + "\n")

output_file.close()
