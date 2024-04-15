from random import seed
from random import randint

# https://www.youtube.com/watch?v=O2pcNxzlL0Q
class MastermindGrid:
    def __init__(self, niveau):
        # initialisation de la seed des nombres aléatoires en fonction de l'heure
        seed(None)
        # self.grid : grille initiale
        # self.final: grille solution
        # self.copygrid: grille temporaire en cas de plusieurs solutions
        self.gridEasy = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.gridFinalEasy = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.gridMedium = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        """[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]"""

        self.gridFinalMedium = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        """[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]"""

        self.gridDifficult = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        """ [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]"""

        self.gridFinalDifficult = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        """ [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]"""
        self.level = niveau

        # initialisation du nombre de zeros et du nombre de solutions

    def affiche(self):
        print("self.grid")
        nbzero=0
        #pour connaitre le nombre de 0 présents dans la grille self.grid
        #et l'afficher dans le terminal
        if self.level == "1" :
            print(self.gridEasy)
            print(self.gridFinalEasy)
            """for i in range(0, len(self.gridEasy)):
                for j in range(0, len(self.gridEasy[0])):
                    print(self.gridEasy[i][j], end=" ")
            print(self.gridEasy[i][j])"""
        elif self.level == "2" :
            print(self.gridMedium)
            print(self.gridFinalMedium)
            """for i in range(0, len(self.gridMedium)):
                for j in range(0, len(self.gridMedium[0])):
                    print(self.gridMedium[i][j], end=" ")"""
            print()
        elif self.level == "3" :
            print(self.gridDifficult)
            print(self.gridFinalDifficult)
            """for i in range(0, len(self.gridDifficult)):
                for j in range(0, len(self.gridDifficult[0])):
                    print(self.gridDifficult[i][j], end=" ")
            print()"""

    # Création grille avec une diagonale 3x3 non vide et valide
    """def start(self):
        self.create()"""

    # Création d'une grille de Sudoku avec xx trous
    def create(self):
        # On recopie la grille solution dans la grille initiale

        # On tire aléatoirement nbEmptyCells valeurs pour faire des trous dans la grille
        # l: nombre de trous
        # nbTours: nombre de tirages aléaroires (max = 100)
        if self.level == "1":
            for i in range(len(self.gridFinalEasy[0])):
                value = randint(1, 3)
                self.gridFinalEasy[0][i] = value
                print(f"i = {i}, value = {value}")
            print("self.gridFinalEasy",self.gridFinalEasy)
            print(self.level)

        elif self.level == "2":
            print(self.level)
            print(f"est self.gridMedium : {len(self.gridFinalMedium[0])}")
            for i in range(len(self.gridFinalMedium[0])):
                value = randint(1, 6)
                self.gridFinalMedium[0][i] = value
                print(f"i = {i}, value = {value}")
            print("self.gridMedium",self.gridMedium)
            print(self.level)

        elif self.level == "3":
            print(self.level)
            for i in range(len(self.gridFinalDifficult[0])):
                value = randint(1, 9)
                self.gridFinalDifficult[0][i] = value
                print(f"i = {i}, value = {value}")
            print("self.gridDifficult",self.gridDifficult)
            print(self.level)


        # self.grid contient les zeros et a une unique solution
        # on recalcule self.final pour avoir la grille solution

    # Pour recuperer la grille avec les zeros
    def getGrid(self):
        if self.level == "1":
            return self.gridEasy
        if self.level == "2":
            return self.gridMedium
        if self.level == "3":
            return self.gridDifficult

    # Pour initilaiser le jeu avec nbEmptyCells zeros (difficile d'avoir une solution unique au dela de 55 cellules vides)
    def reset(self):
        # Creation d'une grille avec la diagonlae 3x3 remplie
        # self.start()
        # On résoud la grille complète de Sudoku
        self.create()
        self.affiche()

    # Pour recuperer la grille solution
    def getFinalGrid(self):
        if self.level == "1":
            return self.gridFinalEasy
        elif self.level == "2":
            return self.gridFinalMedium
        elif self.level == "3":
            return self.gridFinalDifficult
"""
   def getNbZeros(self):
        return self.nbZeros
"""

"""    def main():
        toto=SudokuGrid()
        toto.reset()"""
"""newGrid = MastermindGrid("2")
newGrid.create()
newGrid.affiche()
#newGrid.reset()

newGrid = MastermindGrid("3")
newGrid.create()
newGrid.affiche()"""