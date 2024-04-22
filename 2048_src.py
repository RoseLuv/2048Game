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
        for _ in range(2): # Fills the 2 beginning rows
            fill_cell_w2(self.matrix)
        

def fill_cell_w2(matrix: Matrix):
    while True:
        row = randint(0, len(matrix))
        col = randint(0, len(matrix[0]))
        if matrix[row][col] == '0':
            matrix[row][col] = '2'
            return
    

def move_up(matrix: Matrix):
    return

def move_down(matrix:Matrix):
    return

def move_right(matrix:Matrix):
    return

def move_left(matrix:Matrix):
    return

COMMANDS = {
    'w': move_up,
    's': move_down,
    'd': move_right,
    'a': move_left
}

def main():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    
    game_matrix = matrix(width, height)
    
    while True:
        command = input("Enter command:\n'quit' to exit\n'w' to move up\n's' to move down\n'a' to move left\n'd' to move right ")
        
    
if __name__ == "__main__":
    main()
    
    
    



x = matrix(4,4)
