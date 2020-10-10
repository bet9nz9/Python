import re

input_file = open("input.txt", "r")

input_str = input_file.readline()

pattern = r'key'

input_str = re.sub(pattern, r'KEY', input_str)

input_file.close()

input_file = open("input.txt", "w")

input_file.write(input_str)

input_file.close()
