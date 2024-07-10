"""."""

class Verifier_la_condition_de_victoire(Board):

    def __init__(self, rows, columns):
        Board.__init__(self, rows, columns)
    
    def verifier_cond(self, grid, pion):

        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] == self.pion:

                    col + 3 < self.columns and all(self.grid[col][col+1] == pion for i in rang(4)):
                    return True










    


        raise NotImplementedError