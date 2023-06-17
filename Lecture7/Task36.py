def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = map(str, (operation(i, j) for j in range(1, num_columns+1)))
        print(' '.join(row))

print_operation_table(lambda x, y: x * y)
