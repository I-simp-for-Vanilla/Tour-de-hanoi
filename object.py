from var import *

class Button(pygame.sprite.Sprite):

    def __init__(self, role : str, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.role = role
        self.image = pygame.Surface((200, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.image.fill(white)

    def update(self):
        
        screen.blit(self.image, self.rect)

    def click(self):
        if self.role == "start":
            TowerA = Tower(1)
            TowerB = Tower(2)
            TowerC = Tower(3)

            all_towers.add(TowerA)
            all_towers.add(TowerB)
            all_towers.add(TowerC)

            for i in range(level):
                disk = Disk(level-i, HEIGHT-25*i)
                all_disks.add(disk)
                TowerA.empile(disk)

class Disk(pygame.sprite.Sprite):

    def __init__(self, id : int, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.image = pygame.Surface((50 + 30*self.id, 25))
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = WIDTH*0.25
        self.image.fill(white)
        self.text = ARIAL.render(str(id), 1, black)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def display(self, rect, text_rect):
        screen.blit(self.image, rect)
        screen.blit(self.text, text_rect)

class Tower(pygame.sprite.Sprite):

    def __init__(self, id : int):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.image = pygame.Surface((10, 500))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.centerx = int(WIDTH*0.25*self.id)
        self.image.fill(white)
        self.content = []

    def update(self):
        screen.blit(self.image, self.rect)
        self.display_disks()

    def empile(self, disk):
        self.content.append(disk)

    def depile(self):
        return self.content.pop(len(self.content)-1)
    
    def pileHead(self):
        return self.content[len(self.content)-1]
    
    def display_disks(self):
        for i in range(len(self.content)):
            rect = self.content[i].image.get_rect()
            rect.bottom = HEIGHT-i*25
            rect.centerx = self.rect.centerx
            text_rect = self.content[i].text.get_rect()
            text_rect.center = rect.center
            self.content[i].display(rect, text_rect)

all_towers = pygame.sprite.Group()
all_disks = pygame.sprite.Group()

TowerA = Tower(1)
TowerB = Tower(2)
TowerC = Tower(3)

all_towers.add(TowerA)
all_towers.add(TowerB)
all_towers.add(TowerC)

for i in range(level):
    disk = Disk(level-i, HEIGHT-25*i)
    all_disks.add(disk)
    TowerA.empile(disk)