from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import functools
import numpy as np
from SudokuGrid import *
from MastermindGrid import *
from fichierScore import *

#####################################
########### Page d'accueil ##########
#####################################

class FirstWindow (QWidget):    #QMainWindow
    def __init__(self,nom,prenom,age):
        super().__init__()
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.setWindowTitle("Sudoku")
        self.setMinimumSize(470, 375)
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QColor(51,209,255))  # couleur de fond
        self.setPalette(pal)
        self.level = -1
        self.boutonCheck = False

        self.boite = QVBoxLayout()
        self.grille = QGridLayout()

        self.setIdentifiants()
        self.saisiNiveau()
        self.setBoutons()

        self.grille.setHorizontalSpacing(0)
        self.grille.setVerticalSpacing(15)
        self.grille.setAlignment(Qt.AlignCenter)
        self.boite.addLayout(self.grille)
        self.setLayout(self.boite)

        """print("facileBouton", facileBouton.isChecked())
        print("moyenBouton", moyenBouton.isChecked())
        print("DifficilBouton", AvanceBouton.isChecked())"""

    def setBoutons(self):
        boutonRadio = ["niveau : 1", "niveau : 2", "niveau : 3"]
        boutons = [] #les niveaux
        for i in range(len(boutonRadio)):
            boutons.append(QRadioButton(boutonRadio[i]))
            self.grille.addWidget(boutons[i], i + 30, 0)
        facileBouton = boutons[0]
        moyenBouton = boutons[1]
        avanceBouton = boutons[2]
        facileBouton.clicked.connect(self.assignFacil)
        #facileBouton.setChecked(False)
        moyenBouton.clicked.connect(self.assignMoyen)
        #moyenBouton.setChecked(False)
        avanceBouton.clicked.connect(self.assignDifficil)
        #avanceBouton.setChecked(False)

        playBouton = QPushButton("PLAY")
        playBouton.clicked.connect(self.playPartie)
        self.grille.addWidget(playBouton)

    def saisiNiveau(self):
        self.label = QLabel()
        self.label.setText("Saisir votre niveau:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border : black; background :51,209,255; color :black; font : 12pt;")
        self.grille.addWidget(self.label, 5, 0)

        self.label2 = QLabel()
        self.label2.setText("Vous avez oublié de saisir votre niveau !")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("border : black; background :51,209,255; color = black; font : 12pt;")
        self.label2.setVisible(False)
        self.grille.addWidget(self.label2, 15, 0)

    def setIdentifiants(self):
        labelNom = QLabel()
        labelNom.setText("Nom: " + self.nom)
        labelNom.setAlignment(Qt.AlignCenter)
        labelNom.setStyleSheet("border : black; background :51,209,255; color = black; font : 15pt;")

        labelPrenom = QLabel()
        labelPrenom.setText("Prenom : " + self.prenom)
        labelPrenom.setAlignment(Qt.AlignCenter)
        labelPrenom.setStyleSheet("border : black; background :51,209,255; color = black; font : 15pt;")

        labelAge = QLabel()
        labelAge.setText("Age : " + str(self.age))
        labelAge.setAlignment(Qt.AlignCenter)
        labelAge.setStyleSheet("border : black; background :51,209,255; color = black; font : 15pt;")

        self.grille.addWidget(labelNom, 0, 0)
        self.grille.addWidget(labelPrenom, 1, 0)
        self.grille.addWidget(labelAge, 2, 0)

    def assignFacil(self):
        self.level = 1
        self.boutonCheck = True
        #print("niveau 1")

    def assignMoyen(self):
        self.level = 2
        self.boutonCheck = True
        # print("niveau 2")

    def assignDifficil(self):
        self.level = 3
        self.boutonCheck = True
        # print("niveau 3")

    def playPartie(self):
        if self.boutonCheck == True :
            self.window = MainWindow(str(self.level), self.nom, self.prenom, str(self.age))
            self.window.show()
            self.close()
        else :
            self.label2.setVisible(True)

#################################
########## Page de jeu ##########
#################################

class MainWindow(QMainWindow):
    def __init__(self,niveau, nom, prenom, age):
        super().__init__()
        self.setWindowTitle("Sudoku")  # nom de la fenetre
        self.setMinimumSize(540,540)
        #self.setStyleSheet("background : pink")
        """pal = QPalette()
        pal.setColor(self.backgroundRole(), QColor("white"))
        self.setPalette(pal)"""
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.main_widget = Window(niveau,nom,prenom,age)
        self.main_widget.start()
        self.setCentralWidget(self.main_widget)
        self.setMenuBar()
        #self.setScore()

    """def setScore(self):
        self.scoreEasy = ["Facile","No time","No error","No name","No name","No age"]
        self.scoreMedium = ["Moyen","No time", "No error", "No name", "No name", "No age"]
        self.scoreHard = ["Difficile","No time", "No error", "No name", "No name", "No age"]"""

    def setMenuBar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        game = self.menu_bar.addMenu("Game")
        """menu = QAction("Main Menu", self)
        menu.triggered.connect(self.mainMenu)
        game.addAction(menu)"""

        niveau = game.addMenu("Level")
        niv1 = QAction("Level 1",self)
        niv1.triggered.connect(self.main_widget.niveau1)
        niveau.addAction(niv1)
        niv2 = QAction("Level 2", self)
        niv2.triggered.connect(self.main_widget.niveau2)
        niveau.addAction(niv2)
        niv3 = QAction("Level 3", self)
        niv3.triggered.connect(self.main_widget.niveau3)
        niveau.addAction(niv3)

        restart = QAction("Restart", self)
        restart.triggered.connect(self.main_widget.replayPartie)
        game.addAction(restart)
        quitter = QAction("Quitter", self)
        quitter.triggered.connect(self.close)
        game.addAction(quitter)

        timer = self.menu_bar.addMenu("Timer")
        start = QAction("Start", self)
        start.triggered.connect(self.main_widget.start)
        timer.addAction(start)
        pause = QAction("Pause", self)
        pause.triggered.connect(self.main_widget.pause)
        timer.addAction(pause)
        reset = QAction("Reset", self)
        reset.triggered.connect(self.main_widget.reset)
        timer.addAction(reset)

        high_score = QAction("High Score",self)
        high_score.triggered.connect(self.showHighScore)
        self.menu_bar.addAction(high_score)


    """def mainMenu(self):
        self.windowMenu = FirstWindow(self.nom,self.prenom,self.age)
        self.windowMenu.show()
        self.close()"""

    def showHighScore(self):
        self.windowScore = WindowHighScore(self.main_widget.scoreEasy,self.main_widget.scoreMedium,self.main_widget.scoreHard)
        self.windowScore.setMinimumSize(600, 200)
        self.windowScore.show()

    def jeuFini(self):
        if not self.main_widget.playGame:
            self.showHighScore()



class Window(QWidget):

    def __init__(self,niveau, nom, prenom, age):
        super().__init__()
        self.setMinimumSize(470, 375)
        self.level = niveau
        print(f"est le niveau {niveau} de type : {type(niveau)}")
        self.nom = nom
        self.prenom = prenom
        self.age = age
        #self.erreurs = 0
        self.nbHelp = 3
        self.playGame = True
        self.nb = 0
        self.bornRowHigh = 10
        self.bornRowLow = 11
        self.greatPlace = 0
        self.greatNumber = 0


        #self.pal = QPalette()
        #self.pal.setColor(self.backgroundRole(), QColor(25, 200, 94))  # couleur de fond
        #self.setPalette(self.pal)

        self.createBoutons()
        self.ide()
        self.comboBox()
        self.setChrono()
        self.assignNiveau()
        self.numberCol()

        self.createGrille()
        self.putValues()

        #        https: // stackoverflow.com / questions / 52778141 / qtableview - selecion - change
        self.table.clicked.connect(self.onClickedRow)
        self.selectedCell = [-1, - 1]
        self.createBox()
        self.setScore()

    def createBox(self):
        self.boite = QVBoxLayout()
        self.boite.addLayout(self.grilleIde)
        self.boite.addWidget(self.table)
        self.boite.addLayout(self.grilleChiffres)
        self.setLayout(self.boite)

    def setScore(self):
        self.bestTime = [0,0,0]
        self.scoreEasy = ["Facile","","","","",""]
        self.scoreMedium = ["Moyen","", "", "", "", ""]
        self.scoreHard = ["Difficile","", "", "", "", ""]
        self.windowScore = WindowHighScore(self.scoreEasy,self.scoreMedium,self.scoreHard)

    def numberCol(self):
        if self.level == "1":
            self.lenLineGrid = 4#number of column
        elif self.level == "2":
            self.lenLineGrid = 4
        elif self.level == "3":
            print("est niveau 3")
            self.lenLineGrid = 4
        #self.tabComparaison = []
        self.tabEnter = np.zeros(self.lenLineGrid)
        self.inexTabEnter = 0

    def createGrille(self):
        #newGrid = SudokuGrid()
        newGrid = MastermindGrid(self.level)
        #newGrid.solve()

        newGrid.reset()
        self.gridInit = newGrid.getGrid()
        self.gridFinal = newGrid.getFinalGrid()
        self.tabRandomLine = self.gridFinal[0]
        print("self.tabRandomLine = ,",self.tabRandomLine)
        print("self.tabRandomLine[0] = ", self.tabRandomLine[0])
        self.table = QTableWidget()

        self.table.setRowCount(11)
        print("number of column",self.lenLineGrid)
        self.table.setColumnCount(self.lenLineGrid)
        # permet d'éviter d'afficher les nom d'axes horizontaux et verticaux
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.horizontalScrollBar().setDisabled(True)
        self.table.verticalScrollBar().setDisabled(True)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        for line in range(11):
            self.table.setRowHeight(line, 1)
        for col in range(self.lenLineGrid):
                self.table.setColumnWidth(col, 2)
        for line in range(11):
            for col in range(self.lenLineGrid):
                self.table.setItem(line, col, QTableWidgetItem())

    def assignNiveau(self):
        #nombre de case vides à compléter selon le niveau
        self.nbCasesVides = 0
        print("type=", type(self.level))

        if self.level == "1":
            self.nbCasesVides = 0
            self.lenLineGrid = 4
            print("self.nbCasesVides1=", self.nbCasesVides)
        elif self.level == "2":
            self.nbCasesVides = 0
            self.lenLineGrid = 4
            print("self.nbCasesVides2=", self.nbCasesVides)
        elif self.level == "3":
            self.nbCasesVides = 0
            self.lenLineGrid = 4
            print("self.nbCasesVides3=", self.nbCasesVides)

    def createBoutons(self):
        self.grilleChiffres = QGridLayout()
        boutons = []
        for i in range(9):
            unBouton = QPushButton(str(i + 1))
            # https://wiki.qt.io/Qt_for_Python_Tutorial_ClickableButton
            # https://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
            unBouton.clicked.connect(functools.partial(self.assignValue, str(i + 1)))
            boutons.append(unBouton)
            self.grilleChiffres.addWidget(boutons[i], 2 - i // 3, i % 3)
        self.grilleChiffres.setHorizontalSpacing(0)
        self.grilleChiffres.setVerticalSpacing(0)

    def comboBox(self):
        self.comboBox = QComboBox()
        self.comboBox.setEditable(False)
        listColors = ["white", "blue", "green", "cyan", "yellow", "brown", "red","pink", "purple"]
        self.comboBox.addItems(listColors)
        self.grilleIde.addWidget(self.comboBox, 1, 1)
        self.comboBox.activated.connect(self.changeColor)

    def changeColor(self):
        couleur = self.comboBox.currentText()
        self.setStyleSheet("background : " + couleur)
        """if couleur == "white":
            self.pal.setColor(self.backgroundRole(), QColor(256, 256, 256))  # couleur de fond
        elif couleur == "blue":
            print("ici bleu")
            self.pal.setColor(self.backgroundRole(), QColor(0, 0, 0))  # couleur de fond
            self.setStyleSheet("background : " + couleur)
        else :
            self.setStyleSheet("background : " + couleur)"""

    def assignValue(self, valeurbouton):
        print("le niveau est self.level : ",self.level)
        row = self.selectedCell[0]
        column = self.selectedCell[1]  # bug si aucune case n'est sélectionnée
        print(f"row = {row} and column = {column}")
        print(f"self.bornRowLow = {self.bornRowLow} and self.bornRowHigh = {self.bornRowHigh}")
        numLow = self.bornRowLow
        numHigh = self.bornRowHigh
        if row >= self.bornRowHigh and row < self.bornRowLow and column >= 0 and column < self.lenLineGrid:
            print("i am not in if valeurCellule == """)
            it = self.table.item(row, column)
            valeurCellule = it.text()
            print(valeurCellule)

            if valeurCellule == "":
                print("i am in if valeurCellule == """)
                it.setText(valeurbouton)
                it.setBackground(QColor(150, 110, 100))
                it.setTextAlignment(Qt.AlignCenter)
                it.setFlags(it.flags() & ~Qt.ItemIsSelectable)
                print("nbCaseFilled", self.nbCaseFilled)
                self.nbCaseFilled += 1
                print("self.tabRandomLine : ", self.tabRandomLine)
                print("self.gridFinal[0] : ", self.gridFinal[0])
                self.tabEnter[column] = int(valeurbouton)
                self.inexTabEnter +=1
                tabBase = self.tabRandomLine
                print("tabEnter : ",self.tabEnter)

                if self.nbCaseFilled == self.lenLineGrid :
                    """for i in range(len(self.tabRandomLine)):
                        if str(self.tabRandomLine[i]) == self.tabEnter[i]:
                            print("rien")
                            self.greatPlace += 1"""

                    print(self.tabEnter)
                    self.nbCaseFilled = 0
                    print("je suis au changement nbCaseFilled = ", self.nbCaseFilled)
                    self.bornRowLow -= 1
                    self.bornRowHigh -= 1
                    tabRestingValues=self.rem(tabBase, self.tabEnter, len(tabBase))
                    self.greatPlace = tabRestingValues[0]
                    self.greatNumber = tabRestingValues[1]
                    print(" tabRestingValues : ",tabRestingValues)
                    #self.greatNumber = self.lenLineGrid - self.greatPlace -len(tabRestingValues)
                    print("nombre de mal placés : ",self.greatNumber)
                    print("nombre de bien placés", self.greatPlace)
                    print(f"self.lenLineGrid = {self.lenLineGrid}and self.greatPlace {self.greatPlace}")
                    self.nbErreurs()
                    if self.greatPlace == self.lenLineGrid:
                        print("wiinnnnnn")
                        self.endGame()
                    self.greatPlace = 0
                    self.greatNumber = 0
                    self.tabEnter = np.zeros(self.lenLineGrid)
            nb = 0
            for line in range(9):
                for col in range(self.lenLineGrid):
                    it = self.table.item(line, col)
                    valeurCellule = it.text()
                    if valeurCellule != "":
                        nb += 1
            self.nb = nb
            print("nombre =", self.nb)
            self.table.update()
            QApplication.processEvents()
            if self.nb == self.lenLineGrid*11 :
                self.endGameLose()


    def putValues(self):
        for line in range(11):
            for col in range(self.lenLineGrid):
                it = self.table.item(line, col)
                it.setText("")
                it.setBackground(QColor(256, 256, 256))
                it.setForeground(QColor(0, 0, 0))
                it.setFlags(it.flags() & ~Qt.ItemIsEditable)
                it.setTextAlignment(Qt.AlignCenter)
                if self.gridInit[line][col] != 0:
                    it.setText(str(self.gridInit[line][col]))
                    it.setBackground(QColor(100, 110, 10))
                    it.setForeground(QColor(0, 0, 0))
                    it.setFlags(it.flags() & ~Qt.ItemIsSelectable)
                    it.setTextAlignment(Qt.AlignCenter)
        self.update()

    def onClickedRow(self, index=None):
        #print(index.row(), index.column())
        self.selectedCell = [index.row(), index.column()]

    def ide(self):
        self.labelNiveau = QLabel()
        self.labelNiveau.setText("Niveau : " + str(self.level))
        self.labelNiveau.setAlignment(Qt.AlignCenter)
        self.labelNiveau.setStyleSheet("background :orange; color : black; font : 12pt;")

        self.helpButton = QPushButton()
        self.helpButton.setText("3")
        self.helpButton.setIcon(QIcon('help_icon.png'))
        self.helpButton.clicked.connect(self.askHelp)

        self.grilleIde = QGridLayout()
        self.grilleIde.addWidget(self.labelNiveau,0,0)
        self.grilleIde.addWidget(self.helpButton,1,0)

    def setChrono(self):
        self.time = 0
        self.flag = False
        self.label = QLabel()
        self.labelErreurs =QLabel()
        self.labelErreurs.setText("Greate PLace :  "+str(self.greatPlace) + "\nBadPLace : "+str(self.greatNumber))

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background : yellow; color: black; font : 12pt;")
        # self.label.adjustSize()

        self.labelErreurs.setStyleSheet("background : pink; color: black; font : 12pt;")
        self.labelErreurs.setAlignment(Qt.AlignCenter)
        #self.grilleTime.addWidget(self.labelErreurs,1,0)
        self.grilleIde.addWidget(self.labelErreurs,0,1)
        self.grilleIde.addWidget(self.label, 0, 2)

        #self.grilleTime.addWidget(self.label, 0, 0)
        #self.grilleTime.setAlignment(Qt.AlignRight)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)#pour qu'on puisse avoir le temps en seconde *10, autrement sans le parametre le compteur défile trop vite

    def nbErreurs(self):
        #self.erreurs += 1
        self.labelErreurs.setText("Greate PLace :  "+str(self.greatPlace) + "\nBadPLace : "+str(self.greatNumber))#str(self.erreurs))
        print("Greate PLace :  "+str(self.greatPlace) + "\nBadPLace : "+str(self.greatNumber))

    def askHelp(self):
        row = self.selectedCell[0]
        column = self.selectedCell[1]
        if row >= 0 and row < 9 and column >= 0 and column < self.lenLineGrid:
            it = self.table.item(row, column)
            valeurCellule = it.text()
            print(valeurCellule)
            if valeurCellule == "":
                if self.nbHelp > 0:
                    self.nbHelp -= 1
                    self.helpButton.setText(str(self.nbHelp))
                    self.assignValue(str(self.gridFinal[row][column]))
                    self.time += 100  # si on fait appel à de l'aide : pénalité de 10secondes
                    if self.nbHelp == 0:
                        self.helpButton.setEnabled(False)

    def showTime(self):
        if self.flag :
            self.time += 1
        self.texte = str(self.time / 10)#1 chiffre après la virgule(et le temps en seconde)
        self.label.setText("Chrono :" + self.texte)

    def start(self):
        self.flag = True
        self.nbCaseFilled = 0
        self.bornRowLow = 11
        self.bornRowHigh = 10

    def pause(self):
        self.flag = False

    def reset(self):
        self.flag = True
        self.time = 0
        self.playGame = True

    def resetError(self):
        #self.erreurs = -1
        self.nbErreurs()

    def replayPartie(self):
        self.bornRowHigh = 10
        self.bornRowLow = 11
        self.greatPlace = 0
        self.greatNumber = 0
        self.nbCaseFilled = 0
        self.numberCol()
        print("self.level =", self.level)
        newGrid = MastermindGrid(self.level)
        newGrid.create()
        newGrid.affiche()


        print("number of column", self.lenLineGrid)
        self.gridInit = newGrid.getGrid()
        self.gridFinal = newGrid.getFinalGrid()
        self.tabRandomLine = self.gridFinal[0]
        self.putValues()
        self.update()
        self.reset()
        self.resetError()
        self.nbHelp = 3
        self.helpButton.setEnabled(True)
        self.helpButton.setText("3")
        self.windowScore.setVisible(False)

    def niveau1(self):
        self.changeNiveau(1)

    def niveau2(self):
        self.changeNiveau(2)

    def niveau3(self):
        self.changeNiveau(3)

    def changeNiveau(self,niveau):
        print("je suis passé par changeNIveau")
        if niveau == 1:
            self.level = "1"
            self.labelNiveau.setText("Niveau : " + self.level)
        elif niveau == 2:
            self.level = "2"
            self.labelNiveau.setText("Niveau : " + self.level)
        elif niveau == 3:
            self.level = "3"
            self.labelNiveau.setText("Niveau : " + self.level)
        print("self.level à changeNIveau, ",self.level)
        self.replayPartie()

    def putScore(self):
        if self.level == "1":
            self.scoreEasy[1] = str(self.bestTime[0]/10)
            self.scoreEasy[2] = 0#str(self.erreurs)mettre le nombre d'aides
            self.scoreEasy[3] = self.prenom
            self.scoreEasy[4] = self.nom
            self.scoreEasy[5] = str(self.age)

        if self.level == "2":
            self.scoreMedium[1] = str(self.bestTime[1]/10)
            self.scoreMedium[2] = 0#str(self.erreurs)
            self.scoreMedium[3] = self.prenom
            self.scoreMedium[4] = self.nom
            self.scoreMedium[5] = str(self.age)

        if self.level == "3":
            self.scoreHard[1] = str(self.bestTime[2]/ 10)
            self.scoreHard[2] = 0#str(self.erreurs)
            self.scoreHard[3] = self.prenom
            self.scoreHard[4] = self.nom
            self.scoreHard[5] = str(self.age)

    def endGame(self):
        self.pause()
        tabScore = readScore()
        self.scoreEasy = tabScore[0]
        self.scoreMedium = tabScore[1]
        self.scoreHard = tabScore[2]

        if self.level == "1":

            if self.scoreEasy[1] == "":
                self.bestTime[0] = self.time
                self.putScore()
            else :
                temps=float(self.scoreEasy[1])*10
                if self.time < temps:
                    self.bestTime[0] = self.time
                    self.putScore()
        if self.level == "2":
            if self.scoreMedium[1] == "":
                self.bestTime[1] = self.time
                self.putScore()
            else :
                temps = float(self.scoreMedium[1]) * 10
                if self.time < temps:
                    self.bestTime[1] = self.time
                    self.putScore()
        if self.level == "3":
            if self.scoreHard[1] == "":
                self.bestTime[2] = self.time
                self.putScore()
            else :
                temps = float(self.scoreHard[1]) * 10
                if self.time < temps:
                    self.bestTime[2] = self.time
                    self.putScore()
        tabScore=[self.scoreEasy,self.scoreMedium,self.scoreHard]
        writeScore(tabScore)
        self.windowScore = WindowHighScore(self.scoreEasy,self.scoreMedium,self.scoreHard)
        self.boite.addWidget(self.windowScore)

    def rem(self,tabBase, tabEnter, lentab):
        greatPlace =0
        tabB = tabBase
        tabE = tabEnter
        tabCountB = np.zeros(9)
        tabCountE = np.zeros(9)

        for i in range(lentab):
            if tabE[i] == tabB[i]:
                greatPlace +=1
        """for i in range(lentab):
            if tabE[i] in tabB:
                tabB.remove(tabE[i])"""
        for i in range(9):
            tabCountE[i] = tabE.count(i)
            tabCountB[i] = tabB.count(i)

        greatNumber = self.lenLineGrid - greatPlace - len(tabB)
        return [greatPlace,greatNumber]


#################################
########## Page finale ##########
#################################

class FinalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku")
        self.setMinimumSize(650, 250)
        self.main_widget = WindowHighScore()
        self.setCentralWidget(self.main_widget)
        self.setMenuBar()

    def setMenuBar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        game = self.menu_bar.addMenu("Game")
        menu = QAction("Main Menu", self)
        menu.triggered.connect(self.mainMenu)
        game.addAction(menu)
        restart = QAction("Restart", self)
        restart.triggered.connect(self.main_widget.replayPartie)
        game.addAction(restart)
        quitter = QAction("Quitter", self)
        quitter.triggered.connect(self.close)
        game.addAction(quitter)

class WindowHighScore(QWidget):
    def __init__(self,scoreEasy,scoreMedium,scoreHard):
        super().__init__()
        self.setWindowTitle("High Score")
        #self.setMinimumSize(650, 250)
        self.scoreEasy = scoreEasy
        self.scoreMedium = scoreMedium
        self.scoreHard = scoreHard
        self.madeBox()
        self.putScore()

    def madeBox(self):
        self.boite = QVBoxLayout()
        self.table = QTableWidget(4, 6)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.horizontalScrollBar().setDisabled(True)
        self.table.verticalScrollBar().setDisabled(True)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.boite.addWidget(self.table)
        self.setLayout(self.boite)
        for line in range(0, 4):
            for col in range(0, 6):
                self.table.setItem(line, col, QTableWidgetItem())
                self.table.setRowHeight(line, 20)
                self.table.setColumnWidth(col, 80)
        for line in range(0, 4):
            for col in range(0, 6):
                item = self.table.item(line, col)
                item.setText("")
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def putScore(self):
        param = ["Niveau:", "Temps:", "Erreurs:", "Prénom:", "Nom:", "Age:"]
        tabScore =readScore()
        for i in range(0, 6):
            item = self.table.item(0, i)
            item.setText(param[i])
            item.setTextAlignment(Qt.AlignCenter)
        for i in range(0, 6):
            item = self.table.item(1, i)
            #item.setText(self.scoreEasy[i])#lire le fichier 1ère ligne et mettre les valeurs dans les cases scoreTab [0][i]
            item.setText(tabScore[0][i])
            item.setTextAlignment(Qt.AlignCenter)
        for i in range(0, 6):
            item = self.table.item(2, i)
            #item.setText(self.scoreMedium[i])#lire le fichier 2ème ligne et mettre les valeurs dans les cases scoreTab [1][i]
            item.setText(tabScore[1][i])
            item.setTextAlignment(Qt.AlignCenter)
        for i in range(0, 6):
            item = self.table.item(3, i)
            #item.setText(self.scoreHard[i])#lire le fichier 3ème ligne et mettre les valeurs dans les cases scoreTab [2][i]
            item.setText(tabScore[2][i])
            item.setTextAlignment(Qt.AlignCenter)
        self.scoreEasy = tabScore[0]
        self.scoreMedium = tabScore[1]
        self.scoreHard = tabScore[2]