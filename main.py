from object import *

class Game(pygame.sprite.Sprite):

    def __init__(self, id : str):
        pygame.sprite.Sprite.__init__(self)
        self.Running = True
        self.Screennum = 0
        self.caption = pygame.display.set_caption("Tour de Hanoï")
        self.freeDisk = None
        self.buttonStartGame = Button("start", WIDTH//2, HEIGHT//2)
        self.nbMove = 0

    def mainMenu(self):
        """The main menu"""
        pass

    def game(self):
        pass
            

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.Running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.freeDisk == None:
                    if 150 < pygame.mouse.get_pos()[0] < 450 and TowerA.content != []:
                        self.freeDisk = TowerA.depile()
                    elif 450 < pygame.mouse.get_pos()[0] < 750 and TowerB.content != []:
                        self.freeDisk = TowerB.depile()
                    elif 750 < pygame.mouse.get_pos()[0] < 1050 and TowerC.content != []:
                        self.freeDisk = TowerC.depile()
                else :
                    if 150 < pygame.mouse.get_pos()[0] < 450 and (TowerA.content == [] or self.freeDisk.id < (TowerA.pileHead()).id):
                        TowerA.empile(self.freeDisk)
                        self.freeDisk = None
                        self.nbMove += 1
                    elif 450 < pygame.mouse.get_pos()[0] < 750 and (TowerB.content == [] or self.freeDisk.id < (TowerB.pileHead()).id):
                        TowerB.empile(self.freeDisk)
                        self.freeDisk = None
                        self.nbMove += 1
                    elif 750 < pygame.mouse.get_pos()[0] < 1050 and (TowerC.content == [] or self.freeDisk.id < TowerC.pileHead().id):
                        TowerC.empile(self.freeDisk)
                        self.freeDisk = None
                        self.nbMove += 1

        if len(TowerC.content) == level:
            self.Running = False
            print(".\n.\nCongratulation !!! you just achieved to complete this level in {}/{} moves".format(self.nbMove, 2**level-1))

    def updateScreen(self):
        screen.fill(black)
        all_towers.update()

    def startGame(self):
        while self.Running:
            self.eventHandler()

            if self.Screennum == 0:
                self.mainMenu()
            elif self.Screennum == 1:
                self.game()

            self.updateScreen()
            pygame.display.update()
            pygame.display.flip()


newGame = Game("game")
newGame.startGame()