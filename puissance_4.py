class Tableau(object):
    "Classe tableau du jeu"
    def __init__(self):
        self.affichage = affichage()
    def affichage(self):
        msg1 = [' '+str(i) for i in range(8)]
        return msg1
    
board = Tableau()




print(board.affichage)