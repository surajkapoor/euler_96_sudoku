import numpy as np
import sys
import pdb


nLayers = 0
class SodukuBoard:
    BOARD_SIZE = 9
    VALID = np.arange(1,10)

    board_np = np.zeros([BOARD_SIZE, BOARD_SIZE])
    board = [[0] * BOARD_SIZE ] * BOARD_SIZE
    ref_board = []

    def read_boards_from_txt(self):
        # The idiomatic way to handle file reading
        with open('sudoku.txt', 'r') as file_handle:
            ref_board = []
            for line in file_handle:
                if line[0]=='G':
                    # New board
                    board_number = int(line.split(' ')[1]) - 1
                    ref_board.append(board_number)
                    ref_board[board_number] = []
                    print board_number
                else:
                    print(line)
                    new_board_row = [int(c) for c in line if c in '1234567890']
                    ref_board[board_number].append(new_board_row)

            self.ref_board = ref_board
            self.ref_board_np = np.array(ref_board)

    def check_rows(board_np):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(board_np[i,:])) < BOARD_SIZE:
                return False
        return True

    def check_columns(board_np):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(board_np[:,i])) < BOARD_SIZE:
                return False
        return True

    def check_sub_boards(board_np):
        # Need to run through each subboard, there are nine ... and
        return

    def validate_solution(board_np):
        if check_rows(board_np):
            if check_columns(board_np):
                if check_sub_boards(board_np):
                    return True

    def search_for_weak_spot(self, board_np):
        # How is board_size scoped??? Why isn't it appearing here.

        for r in xrange(0,9):
            for c in xrange(0,9):
                grid[r][c] = []
                if board_np[r, c] != 0:
                        continue
                possible_sols = []
                for i in xrange(1,10):
                    board_np[r,c] = i
                    if self.check_row(board_np, r) and self.check_col(board_np, c) and self.check_sub_board(board_np, r/3, c/3):
                        possible_sols.append(i)
                    board_np[r, c] = 0

                print "Possible sols for element [%d,%d]: %r" %(r, c, possible_sols)
                grid[r][c].append(possible_sols)
                if len(possible_sols) == 1:
                    board_np[r, c] = possible_sols[0]
                    self.search_for_weak_spot(board_np)
        if board_np.min() != 0:
            print "Board is solved"
        else:
            print grid
            pdb.set_trace()

        return 

    def check_row(self, board_np, row):
        temp = sum(board_np[row,:])
        r = np.unique(board_np[row,:])
        temp2 = sum(r)

        if temp == temp2:
            return True

        return False

    def check_col(self, board_np, col):
        temp = sum(board_np[:,col])
        c = np.unique(board_np[:,col])
        temp2 = sum(c)

        if temp == temp2:
            return True

        return False

    def check_sub_board(self, board_np, row, col):
        a = []
        for r in xrange(0,3):
            for c in xrange(0,3):
                a.append(board_np[3*row+r, 3*col+c])
        #if row == 2 and col ==1:
        #    pdb.set_trace()
        
        temp = sum(a)
        b = np.unique(a)
        temp2 = sum(b)
        if temp == temp2:
            return True
        return False

def make_possibility_grid():
    grid = []

    for i in xrange(0,9):
        grid.append([])
        for j in xrange(0,9):
            grid[i].append([])

    return grid

def main():
    my_board = SodukuBoard()
    my_board.read_boards_from_txt()

    i = 0
    for current_board in my_board.ref_board_np:
        print "Current board: %d" % i
        my_board.search_for_weak_spot(current_board)
        #print current_board
        i += 1

grid = make_possibility_grid()

if __name__ == '__main__':
    #call function that we need
    sys.exit(main())