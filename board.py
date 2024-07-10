"""
Classe Board: représente l'état et la gestion du plateau de jeu
"""

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