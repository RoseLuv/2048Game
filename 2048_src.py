import tkinter as tk
from random import randint
Matrix =  list[list[int]]


class matrix():
    def __init__(self, width: int, height: int) -> None:


        self.width: int = width
        self.height: int = height
        self.matrix: Matrix = []
        for i in range(height):
            self.matrix.append([])
            for j in range(width):
                self.matrix[i].append([])
                self.matrix[i][j] = '0'
        if self.matrix == []:
            print('Invalid input')
            quit()

        for _ in range(2): # Fills the 2 beginning rows
            fill_cell_w2(self.matrix)
        

def fill_cell_w2(matrix: Matrix):
    while True:
        row = randint(1, len(matrix) - 1)
        col = randint(1, len(matrix[0]) - 1)
        if matrix[row][col] == '0':
            matrix[row][col] = '2'
            return
    

def move_up(matrix: Matrix):
    # First it will move and then it will add the numbers
    return

def move_down(matrix:Matrix):
    return

def move_right(matrix:Matrix):      
    return

def left(matrix:Matrix):
    move_left(matrix)
    add_left(matrix)
    move_left(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
    return

def add_left(matrix:Matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != '0':
                matrix[i][j] = str(int(matrix[i][j]) * 2)
                matrix[i][j + 1] = '0'


def move_left(matrix:Matrix):
    for i in range(len(matrix) - 1):
        pos = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] != '0':
                while matrix[i][pos] != '0':
                    pos += 1
                matrix[i][pos], matrix[i][j] = matrix[i][j], '0'
            pos = 0
    return


COMMANDS = {
    'w': move_up,
    's': move_down,
    'd': move_right,
    'a': left,
}

def main():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    
    game_matrix = matrix(width, height)
    game_matrix.matrix =[
        ['0','0','2','2'],
        ['0','0','2','0'],
        ['0','2','0','0'],
        ['2','0','0','0']
    ]
    print(game_matrix.matrix)
    while True:
        command = input("Enter command:\n'quit' to exit\n\'w' to move up\n's' to move down\n\'a' to move left\n'd' to move right\n")
        if command == 'quit':
            print('Exiting the game...')
            quit()
        if command in COMMANDS:
            COMMANDS[command](game_matrix.matrix)
        else:
            print("Unknown command.")
        
    
if __name__ == "__main__":
    main()
    
    

x = matrix(4,4)


"""
    TEST MATRICES:
    [
        [0,0,0,2],
        [0,0,2,0],
        [0,2,0,0],
        [2,0,0,0]
    ]

"""