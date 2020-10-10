import random

def get_matrix(m, n):
    matrix = []
    for rows in range(0, m):
        matrix.append([])
        for columns in range(0, n):
            matrix[rows].append(round(random.uniform(0, 50)))
    return matrix

def output(matrix):
    for rows in range(0, len(matrix)):
        print(*str(matrix[rows]))

def print_average(matrix):
    for num in range(0, len(matrix)):
        print("Средее отклонение строки №"+str(num)+" : "+str(matrix[num]))

def get_standart_deviation(matrix):
    # average_in_row = 0
    average_of_rows = []
    for rows in range(0, len(matrix)):
        x_dash = 0
        average_in_row = 0
        for cols in range(0, len(matrix[rows])):
            average_in_row += matrix[rows][cols]
        x_dash = average_in_row/len(matrix[rows])
        powed_average_of_row = 0
        for num in range(0, len(matrix[rows])):
            powed_average_of_row += (matrix[rows][num] - x_dash)**2
        average_of_rows.append(powed_average_of_row/len(matrix[rows]))

    return average_of_rows
