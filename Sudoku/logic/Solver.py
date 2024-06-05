from interface.SolverInterface import SolverInterface


class Solver(SolverInterface):
    def solve(self, board):
        """
        Solve the Sudoku puzzle using backtracking.
        :param board: 2D list representing the Sudoku board
        :return: True if the puzzle is solved, False otherwise
        """
        try:
            empty = self.find_empty(board)  # Find the first empty spot on the board
            if not empty:  # If no empty spot is found, the puzzle is solved
                return True  # Puzzle solved
            row, col = empty  # Get the row and column of the empty spot

            for num in range(1, 10):  # Try numbers 1-9
                if self.is_valid(board, num, (row, col)):  # Check if the number is valid in the current position
                    board[row][col] = num  # Place the number on the board

                    if self.solve(board):  # Recursively attempt to solve the rest of the board
                        return True

                    board[row][col] = 0  # Reset the cell on backtrack

            return False  # If no number is valid, backtrack
        except Exception as e:
            print(f"Error solving the board: {e}")
            return False

    def is_valid(self, board, num, position):
        """
        Check if a number is valid in the given position.
        :param board: 2D list representing the Sudoku board
        :param num: Number to be placed
        :param position: Tuple (row, col) representing the position on the board
        :return: True if the number is valid, False otherwise
        """
        try:
            # Check row
            for i in range(len(board[0])):  # Iterate through each column in the row
                if board[position[0]][i] == num and position[1] != i:  # Check if the number already exists in the row
                    return False

            # Check column
            for i in range(len(board)):  # Iterate through each row in the column
                if board[i][position[1]] == num and position[0] != i:  # Check if the number already exists in the column
                    return False

            # Check box
            box_x = position[1] // 3  # Determine the column index of the 3x3 box
            box_y = position[0] // 3  # Determine the row index of the 3x3 box

            for i in range(box_y * 3, box_y * 3 + 3):  # Iterate through each row in the 3x3 box
                for j in range(box_x * 3, box_x * 3 + 3):  # Iterate through each column in the 3x3 box
                    if board[i][j] == num and (i, j) != position:  # Check if the number already exists in the 3x3 box
                        return False

            return True  # If the number is valid in the row, column, and 3x3 box, return True
        except Exception as e:
            print(f"Error validating number {num} at position {position}: {e}")
            return False

    def find_empty(self, board):
        """
        Find an empty space on the Sudoku board.
        :param board: 2D list representing the Sudoku board
        :return: Tuple (row, col) representing the position of an empty space, or None if no empty space
        """
        try:
            for i in range(len(board)):  # Iterate through each row
                for j in range(len(board[0])):  # Iterate through each column
                    if board[i][j] == 0:  # Check if the cell is empty
                        return (i, j)  # Return the position of the empty cell
            return None  # If no empty cell is found, return None
        except Exception as e:
            print(f"Error finding empty cell: {e}")
            return None

    def count_solutions(self, board):
        """
        Count the number of solutions to the Sudoku puzzle.
        :param board: 2D list representing the Sudoku board
        :return: Number of solutions
        """
        empty = self.find_empty(board)
        if not empty:
            return 1
        row, col = empty

        count = 0
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                count += self.count_solutions(board)
                board[row][col] = 0
                if count > 1:
                    break
        return count

    def has_unique_solution(self, board):
        """
        Check if the Sudoku puzzle has a unique solution.
        :param board: 2D list representing the Sudoku board
        :return: True if the puzzle has a unique solution, False otherwise
        """
        return self.count_solutions(board) == 1

    def is_valid_solution(self, board):
        """
        Check if the given board is a valid Sudoku solution.
        :param board: 2D list representing the Sudoku board
        :return: True if the board is a valid solution, False otherwise
        """
        try:
            # Check all rows and columns
            for i in range(9):  # Iterate through each row and column
                row_nums = set()  # Set to track numbers in the current row
                col_nums = set()  # Set to track numbers in the current column
                for j in range(9):  # Iterate through each cell in the row and column
                    row_num = board[i][j]  # Get the number in the current row cell
                    col_num = board[j][i]  # Get the number in the current column cell
                    if row_num == 0 or col_num == 0:  # Ensure no cell is empty
                        return False
                    if row_num in row_nums or col_num in col_nums:  # Ensure no duplicates in rows and columns
                        return False
                    row_nums.add(row_num)  # Add the number to the row set
                    col_nums.add(col_num)  # Add the number to the column set

            # Check all 3x3 subgrids
            for box_start_row in range(0, 9, 3):  # Iterate through each 3x3 subgrid starting row
                for box_start_col in range(0, 9, 3):  # Iterate through each 3x3 subgrid starting column
                    box_nums = set()  # Set to track numbers in the current 3x3 subgrid
                    for row in range(box_start_row, box_start_row + 3):  # Iterate through each row in the 3x3 subgrid
                        for col in range(box_start_col, box_start_col + 3):  # Iterate through each column in the 3x3 subgrid
                            num = board[row][col]  # Get the number in the current cell
                            if num == 0:  # Ensure no cell is empty
                                return False
                            if num in box_nums:  # Ensure no duplicates in the 3x3 subgrid
                                return False
                            box_nums.add(num)  # Add the number to the 3x3 subgrid set

            return True  # The board is valid only if all checks pass
        except Exception as e:
            print(f"Error validating solution: {e}")
            return False
