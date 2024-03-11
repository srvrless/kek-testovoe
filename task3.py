def evaluate_constraints(N, M, Q, columns, table, constraints):
    total_sum = 0

    for row in table:
        satisfy_all_constraints = True
        for constraint in constraints:
            column_name, operator, value = constraint
            column_index = columns.index(column_name)
            cell_value = row[column_index]

            if operator == "<":
                if not (cell_value < value):
                    satisfy_all_constraints = False
                    break
            elif operator == ">":
                if not (cell_value > value):
                    satisfy_all_constraints = False
                    break

        if satisfy_all_constraints:
            total_sum += sum(row)

    return total_sum


N, M, Q = map(int, input().split())
columns = input().split()
table = [list(map(int, input().split())) for _ in range(N)]
constraints = [input().split() for _ in range(Q)]
constraints = [
    (constraint[0], constraint[1], int(constraint[2])) for constraint in constraints
]

result = evaluate_constraints(N, M, Q, columns, table, constraints)
print(result)
