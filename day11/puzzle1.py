"""
Based on Martin Andersson implementation of Game of Life
https://medium.com/better-programming/how-to-write-conwells-game-of-life-in-python-c6eca19c4676
"""

import os

class Cell:
    def __init__(self):
        '''
        Class holding init status of cell (floor).
        Ability to set- and fetch new statuses with functions
        '''
        self._status = 'Floor'

    def set_floor(self):
        '''
        method sets the cell status to empty
        '''
        self._status = 'Floor'

    
    def set_empty(self):
        '''
        method sets the cell status to empty
        '''
        self._status = 'Empty'

    def set_occupied(self):
        '''
        method sets the cell status to occupied
        '''
        self._status = 'Occupied'

    def is_occupied(self):
        '''
        method checks if the cell is occupied
        returns True if it is alive, False if not.
        '''
        if self._status == 'Occupied':
            return True
        return False
    
    def is_floor(self):
        
        if self._status == 'Floor':
            return True
        return False

    def is_empty(self):
        
        if self._status == 'Empty':
            return True
        return False

    def get_print_character(self):
        '''
        method returning a status character of our choice to print on the board
        '''
        if self.is_occupied():
            return '#'
        elif self.is_floor():
            return '.'
        return 'L'

'''
Game of Life
Board Class
Martin A. Aaberge
'''

from random import randint

class Board:
    def __init__(self , rows , columns):
        '''
        constructor holds input from user and populates the grid with cells. 
        '''
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        # self._generate_board()

    def draw_board(self):
        '''
        method that draws the actual board in the terminal
        '''
        print('\n'*10)
        print('printing board')
        for row in self._grid:
            for column in row:
                print (column.get_print_character(),end='')
            print () # to create a new line pr. row.

    def generate_board(self):
        '''
        method that sets the random state of all cells.
        '''

        for row in self._grid:
            for column in row:
                chance_number = randint(0,3)
                if chance_number == 1:
                    column.set_floor()
                elif chance_number == 2:
                    column.set_empty()
                else:
                    column.set_occupied()
    
    def load_board(self, lst):

        for row_idx, row in enumerate(self._grid):
            for column_idx, column in enumerate(row):
                if lst[row_idx][column_idx] == 'L':
                    column.set_empty()
                elif lst[row_idx][column_idx] == '#':
                    column.set_occupied()
                else:
                    column.set_floor()


    def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_occupied = []
        gets_empty = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                occupied_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_occupied():
                        occupied_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]

                #If the cell is occupied, check the neighbour status.
                if cell_object.is_empty():
                    if len(occupied_neighbours_count) == 0:
                        goes_occupied.append(cell_object)
                if cell_object.is_occupied():
                    if len(occupied_neighbours_count) >= 4:
                        gets_empty.append(cell_object)

        #set cell statuses

        if len(goes_occupied) == 0 and len(gets_empty) == 0:
            return False

        for cell_items in goes_occupied:
            cell_items.set_occupied()

        for cell_items in gets_empty:
            cell_items.set_empty()

        return True
    
    def check_neighbour(self, check_row , check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''        
        #how deep the search is:
        search_min = -1
        search_max = 2

        #empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list
    
    def calculate_seats(self):
        seats = 0
        for row in self._grid:
            for column in row:
                if column.is_occupied():
                    seats += 1
        return seats


def main():
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print(content)
    
    #assume the user types in a number
    # user_rows = int(input('how many rows? '))
    # user_columns = int(input('how many columns? '))

    rows = len(content)
    columns = len(content[0])
    # create a board:
    game_of_life_board = Board(rows,columns)
    game_of_life_board.load_board(content)

    #run the first iteration of the board:
    game_of_life_board.draw_board()
    #game_of_life_board.update_board()

    user_action = ''
    generation = 0
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            if not game_of_life_board.update_board():
                print(generation)
                print('Seats ', game_of_life_board.calculate_seats())
                break
            game_of_life_board.draw_board()
            generation += 1

if __name__ == "__main__":


    main()
