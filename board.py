"""
Classe Board: représente l'état et la gestion du plateau de jeu
"""
import random

class Board:

    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]

    def afficher_plateau(self):
    
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
            print("-" * (4 * self.columns + 1))
    
    def ajouter_un_pion(self, column, pion):
        
        for row in range(len(self.grid))[::-1]:
            if self.grid[row][column] == ' ':
                self.grid[row][column] = pion
                break
    
        return self.grid
    
    def verifier_colonnes_disponibles(self, grid):

        collones_disponibles = []

        for col in range(self.columns):
            for row in range(len(grid))[::-1]:
                if grid[row][col] == ' ':
                    collones_disponibles.append(col)
                else:
                    pass
        
        collones_disponibles = set(collones_disponibles)
        print(collones_disponibles)


board = Board()

j = 40

while j > 0:
    i = random.choice(range(0, 7))
    grid = board.ajouter_un_pion(i, "X")
    j -= 1

board.afficher_plateau()
board.verifier_colonnes_disponibles(grid)