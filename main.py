from object import *

class Game(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Running = True
        self.Screennum = 0
        self.caption = pygame.display.set_caption("Tour de Hanoï")
        self.freeDisk = None
        self.buttonStartGame = Button("start", WIDTH//2, HEIGHT//2)
        self.buttonLevel1 = Button("Level 1", WIDTH//5, HEIGHT//2)
        self.buttonLevel2 = Button("Level 2", 2*WIDTH//5, HEIGHT//2)
        self.buttonLevel3 = Button("Level 3", 3*WIDTH//5, HEIGHT//2)
        self.buttonLevel4 = Button("Level 4", 4*WIDTH//5, HEIGHT//2)
        self.buttonLevel5 = Button("Level 5", WIDTH//5, 3*HEIGHT//4)
        self.buttonLevel6 = Button("Level 6", 2*WIDTH//5, 3*HEIGHT//4)
        self.buttonLevel7 = Button("Level 7", 3*WIDTH//5, 3*HEIGHT//4)
        self.buttonLevel8 = Button("Level 8", 4*WIDTH//5, 3*HEIGHT//4)
        self.buttonBack = Button("Back", WIDTH//2, 3*HEIGHT//4)
        self.nbMove = 0

        self.title = TITLE.render("Main menu", 1, white)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WIDTH//2
        self.title_rect.centery = HEIGHT//4

        self.levelSelectionTitle = TITLE.render("Level Selection", 1, white)
        self.level_selection_title_rect = self.levelSelectionTitle.get_rect()
        self.level_selection_title_rect.centerx = WIDTH//2
        self.level_selection_title_rect.centery = HEIGHT//4

        self.scoreScreenTitle = TITLE.render("Congratulation !", 1, white)
        self.score_screen_title_rect = self.scoreScreenTitle.get_rect()
        self.score_screen_title_rect.centerx = WIDTH//2
        self.score_screen_title_rect.centery = HEIGHT//4

        self.level = 0
        
    def mainMenu(self):
        """The main menu"""

        screen.blit(self.title, self.title_rect)
        self.buttonStartGame.update()

    def levelSelection(self):
        screen.blit(self.levelSelectionTitle, self.level_selection_title_rect)
        self.buttonLevel1.update()
        self.buttonLevel2.update()
        self.buttonLevel3.update()
        self.buttonLevel4.update()
        self.buttonLevel5.update()
        self.buttonLevel6.update()
        self.buttonLevel7.update()
        self.buttonLevel8.update()

    def game(self):
        all_towers.update()

    def scoreScreen(self):
        scoreAnnouncement = PARAGRAPH.render("You achieved to complete this level in {}/{} moves".format(self.nbMove, 2**self.level-1), 1, white)
        score_announcement_title_rect = scoreAnnouncement.get_rect()
        score_announcement_title_rect.centerx = WIDTH//2
        score_announcement_title_rect.centery = HEIGHT//2

        screen.blit(self.scoreScreenTitle, self.score_screen_title_rect)
        screen.blit(scoreAnnouncement, score_announcement_title_rect)
        self.buttonBack.update()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.Running = False

            if self.Screennum == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttonBack.rect.collidepoint(event.pos):
                        self.Screennum = 0 

            if self.Screennum == 2:
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

                if len(TowerC.content) == self.level:
                    self.Screennum = 3
                    print(".\n.\nCongratulation !!! you just achieved to complete this level in {}/{} moves".format(self.nbMove, 2**self.level-1))

            if self.Screennum == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttonLevel1.rect.collidepoint(event.pos):
                        self.level = 1
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel2.rect.collidepoint(event.pos):
                        self.level = 2
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel3.rect.collidepoint(event.pos):
                        self.level = 3
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel4.rect.collidepoint(event.pos):
                        self.level = 4
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel5.rect.collidepoint(event.pos):
                        self.level = 5
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel6.rect.collidepoint(event.pos):
                        self.level = 6
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel7.rect.collidepoint(event.pos):
                        self.level = 7
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2
                    elif self.buttonLevel8.rect.collidepoint(event.pos):
                        self.level = 8
                        for i in range(self.level):
                            disk = Disk(self.level-i, HEIGHT-25*i)
                            TowerA.empile(disk)
                        self.Screennum = 2

            if self.Screennum == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttonStartGame.rect.collidepoint(event.pos):
                        for i in range(len(TowerA.content)):
                            TowerA.depile()
                        for i in range(len(TowerB.content)):
                            TowerB.depile()
                        for i in range(len(TowerC.content)):
                            TowerC.depile()   
                        self.nbMove = 0
                        self.Screennum = 1
            
    def updateScreen(self):
        screen.fill(black)

    def startGame(self):
        while self.Running:
            self.eventHandler()
            self.updateScreen()

            if self.Screennum == 0:
                self.mainMenu()
            elif self.Screennum == 1:
                self.levelSelection()
            elif self.Screennum == 2:
                self.game()
            elif self.Screennum == 3:
                self.scoreScreen()

            pygame.display.update()
            pygame.display.flip()

newGame = Game()
newGame.startGame()