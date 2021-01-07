import math

def get_size(string_size):
    size_ = [int(x) for x in string_size.split()]
    return size_


def get_matrix(num_rows):
    matrix_ = []
    for line in range(num_rows):
        row = [float(x) for x in input().split()]
        matrix_.append(row)
    return matrix_


def add_matrices(matrix_1, matrix_2, size_x):
    for i in range(size_x[0]):
        for j in range(size_x[1]):
            matrix_1[i][j] += matrix_2[i][j]
    return matrix_1


def multiply_by_constant(matrix_x, const, size_x):
    for i in range(size_x[0]):
        for j in range(size_x[1]):
            matrix_x[i][j] = matrix_x[i][j] * const
    return matrix_x


def get_vectors(matrix_1, matrix_2, size_2):
    row_vectors = []
    col_vectors = []
    for i in matrix_1:
        row_vectors.append(i)
    for i in range(size_2[1]):
        vector = []
        col_vectors.append(vector)
        for j in range(size_2[0]):
            vector.append(matrix_2[j][i])
    return row_vectors, col_vectors


def multiply_vectors(vector1, vector2):
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] * vector2[i])
    return sum(result)


def product_matrix(row_vectors, col_vectors, size_x):
    matrix_x = []
    for i in row_vectors:
        line = []
        for j in range(len(col_vectors)):
            dot = multiply_vectors(i, col_vectors[j])
            line.append(dot)
        matrix_x.append(line)
    return matrix_x


def str_matrix(matrix):
    rows_ = len(matrix)
    cols_ = len(matrix[0])
    for i in range(rows_):
        for j in range(cols_):
            matrix[i][j] = str(matrix[i][j])
    return matrix


def display_result(result_):
    result = str_matrix(result_)
    print("The result is:")
    for i in result:
        print(" ".join(i))


def truncate(number, digits):
    step = pow(10.0, digits)
    return math.trunc(step * number) / step


def real_numbers(matrix):
    result = []
    for i in matrix:
        i = [int(x) if x == 0 else x for x in i]
        result.append(i)
    return result


def trunc(matrix):
    result = []
    for i in matrix:
        i = [truncate(x, 2) if x != 0 else x for x in i]
        result.append(i)
    return result


def transpose_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    user_input = input("Enter your choice: ")
    return user_input


def main_diagonal(matrix, size):
    col_vectors = []
    for i in range(size[1]):
        vector = []
        col_vectors.append(vector)
        for j in range(size[0]):
            vector.append(matrix[j][i])
    return col_vectors


def side_diagonal(col_vectors):
    temp = []
    for col in col_vectors:
        temp.append(col[::-1])
    return temp[::-1]


def vertical_line(matrix):
    vertical = []
    for row in matrix:
        row = row[::-1]
        vertical.append(row)
    return vertical


def horizontal_line(col_vectors, size):
    temp = []
    for col in col_vectors:
        temp.append(col[::-1])
    horizontal = []
    for i in range(size[1]):
        vector = []
        horizontal.append(vector)
        for j in range(size[0]):
            vector.append(temp[j][i])
    return horizontal


def minor(matrix, i, j):
    temp_matrix = []
    for row in range(len(matrix)):
        temp_row = []
        if row != i:
            temp_matrix.append(temp_row)
        for col in range(len(matrix[i])):
            if col != j:
                temp_row.append(matrix[row][col])
    return temp_matrix


def determinant(matrix):
    i = 0
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        result = []
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            temp_matrix = minor(matrix, i, j)
            result.append(element * (-1) ** ((i + 1) + (j + 1)) * determinant(temp_matrix))
        return sum(result)


def cofactor_matrix(matrix):
    cof_matrix = []
    for i in range(len(matrix)):
        cof_row = []
        cof_matrix.append(cof_row)
        for j in range(len(matrix[i])):
            temp_matrix = minor(matrix, i, j)
            cofactor = determinant(temp_matrix)
            result = (-1) ** ((i + 1) + (j + 1)) * cofactor
            cof_row.append(result)
    return cof_matrix


def menu():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        user_input = input("Your choice: ")
        if user_input == "1":
            size1 = get_size(input("Enter size of first matrix: "))
            print("Enter first matrix:")
            matrix1 = get_matrix(size1[0])

            size2 = get_size(input("Enter size of second matrix: "))
            print("Enter second matrix:")
            matrix2 = get_matrix(size2[0])

            if size1[0] != size2[0] or size1[1] != size2[1]:
                print("The operation cannot be performed.")
            else:
                result = add_matrices(matrix1, matrix2, size1)
                display_result(result)

        elif user_input == "2":
            size = get_size(input("Enter size of matrix: "))
            matrix = get_matrix(size[0])
            constant = float(input("Enter constant: "))
            result = multiply_by_constant(matrix, constant, size)
            display_result(result)

        elif user_input == "3":
            size1 = get_size(input("Enter size of first matrix: "))
            print("Enter first matrix:")
            matrix1 = get_matrix(size1[0])

            size2 = get_size(input("Enter size of second matrix: "))
            print("Enter second matrix:")
            matrix2 = get_matrix(size2[0])

            row_vectors, col_vectors = get_vectors(matrix1, matrix2, size2)
            new_size = [size1[0], size2[1]]
            new_matrix = product_matrix(row_vectors, col_vectors, new_size)
            display_result(new_matrix)

        elif user_input == "4":
            user_choice = transpose_menu()
            size = get_size(input("Enter matrix size: "))
            print("Enter matrix:")
            matrix = get_matrix(size[0])
            if user_choice == "1":
                result = main_diagonal(matrix, size)
                display_result(result)

            elif user_choice == "2":
                col_vectors = main_diagonal(matrix, size)
                result = side_diagonal(col_vectors)
                display_result(result)

            elif user_choice == "3":
                result = vertical_line(matrix)
                display_result(result)

            elif user_choice == "4":
                col_vectors = main_diagonal(matrix, size)
                result = horizontal_line(col_vectors, size)
                display_result(result)

        elif user_input == "5":
            size = get_size(input("Enter matrix size: "))
            print("Enter matrix:")
            matrix = get_matrix(size[0])
            result = determinant(matrix)
            print(f"The result is: \n{result}")

        elif user_input == "6":
            size = get_size(input("Enter matrix size: "))
            print("Enter matrix:")
            matrix = get_matrix(size[0])
            det_matrix = determinant(matrix)
            constant = 1 / det_matrix
            c_matrix = cofactor_matrix(matrix)
            tr_c_matrix = main_diagonal(c_matrix, size)
            inverse_matrix = multiply_by_constant(tr_c_matrix, constant, size)
            result = real_numbers(inverse_matrix)
            result = trunc(result)
            display_result(result)

        elif user_input == "0":
            break
        else:
            continue


menu()
