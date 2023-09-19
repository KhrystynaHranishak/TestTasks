from task1.config import MODE, RunMode, DATA_PATH


def mark_cell_visited(i, j, visited_cells, m, n, matrix):
    if i < 0 or j < 0 or i >= m or j >= n or visited_cells[i][j] or matrix[i][j] == 0:
        return
    visited_cells[i][j] = 1
    mark_cell_visited(i - 1, j, visited_cells, m, n, matrix)
    mark_cell_visited(i + 1, j, visited_cells, m, n, matrix)
    mark_cell_visited(i, j - 1, visited_cells, m, n, matrix)
    mark_cell_visited(i, j + 1, visited_cells, m, n, matrix)


def count_islands(m, n, matrix):
    if not matrix:
        return 0

    visited_cells = [[0 for _ in range(n)] for _ in range(m)]

    islands_counter = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited_cells[i][j]:
                mark_cell_visited(i, j, visited_cells, m, n, matrix)
                islands_counter += 1

    return islands_counter


def parse_console_input():

    matrix = []

    while True:
        try:
            m, n = map(int, input("Enter two numbers of matrix size: ").split())
            if m <= 0 or n <= 0:
                raise ValueError("Invalid matrix dimensions.")
            else:
                break
        except Exception:
            print("Incorrect values for matrix size. Please try again")

    for k in range(m):
        while True:
            try:
                row = list(map(int, input(f"Enter {k + 1} row of matrix consists of zeros and ones: ").split()))
                if len(row) != n or not set(row) <= {0, 1}:
                    raise ValueError()
                else:
                    matrix.append(row)
                    break
            except Exception as err:
                print(f"Incorrect values for row in matrix size. It should consists of {n} values: zero or one")
    return m, n, matrix


def parse_file_input(file_name):
    data = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        try:
            if i < len(lines) and not lines[i].strip():
                i += 1
            else:
                rows, cols = map(int, lines[i].split())
                i += 1
                if rows <= 0 or cols <= 0:
                    raise ValueError(f"Invalid matrix dimensions in line {i + 1}")
                matrix = []
                for _ in range(rows):
                    if i >= len(lines):
                        raise ValueError(f"Unexpected end of file after line {i}")
                    row = list(map(int, lines[i].strip().split()))
                    if len(row) != cols:
                        raise ValueError(f"Mismatched row length at line {i}. Expected {cols}, found {len(row)}")
                    if not set(row) <= {0, 1}:
                        raise ValueError(f"Invalid matrix values at line {i}. Expected 0s and 1s.")
                    matrix.append(row)
                    i += 1
                if i >= len(lines):
                    raise ValueError(f"Unexpected end of file after line {i}")
                # Parse expected output
                if i < len(lines) and lines[i].strip():
                    expected_result = int(lines[i].strip())
                else:
                    expected_result = None
                i += 1

                data.append((rows, cols, matrix, expected_result))

        except ValueError as e:
            print(f"Error: {e}")
            return

    return data


if __name__ == "__main__":
    if MODE == RunMode.CONSOLE:
        m, n, matrix = parse_console_input()
        islands = count_islands(m, n, matrix)
        print(f"Number of islands: {islands}")
    if MODE == RunMode.FILE:
        data = parse_file_input(DATA_PATH)
        for example in data:
            islands = count_islands(example[0], example[1], example[2])
            print(f"Number of islands: {islands}")

