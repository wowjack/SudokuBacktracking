from pygame import *

init()

def displayText(text, surface, size, position, color):
    Font = font.Font('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', size)
    write = Font.render(text, True, color)
    rect = write.get_rect()
    rect.center = position
    surface.blit(write,rect)

class cell:
    def __init__(self, rcPosition, parent):
        self.position = rcPosition
        self.dimensions = [75,75]
        self.parent = parent
        self.rect = Rect((self.position[1]*75, self.position[0]*75), (75,75))
        self.image = self.parent.subsurface(self.rect)
        self.color = (100,100,100)
        self.editing = False
        self.num = 0

    def update(self, events):
        if self.editing:
            self.image.fill(self.color)
            self.edit(events)
        if self.num != 0:
            displayText(str(self.num), self.image, 50, (38,38), (0,0,0))
        draw.rect(self.image,(0,0,0),Rect((0,0),(75,75)),1)
        self.isEditing(events)

    def isOn(self):
        objPos = self.image.get_abs_offset()
        mousePos = mouse.get_pos()
        if mousePos[0] > objPos[0] and mousePos[0] < objPos[0] + self.dimensions[0] and mousePos[1] > objPos[1] and mousePos[1] < objPos[1] + self.dimensions[1]:
            return True
        return False

    def isClicked(self, events):
        if self.isOn():
            for e in events:
                if e.type == MOUSEBUTTONUP:
                    return True
        return False

    def isEditing(self,events):
        if self.isClicked(events):
            self.editing = True
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                self.editing = False
            elif e.type == KEYUP:
                if e.key == K_RETURN:
                    self.editing = False

    def clear(self):
        self.num = 0

    def edit(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    self.num = 0
                elif e.key == K_1:
                    self.num = 1
                elif e.key == K_2:
                    self.num = 2
                elif e.key == K_3:
                    self.num = 3
                elif e.key == K_4:
                    self.num = 4
                elif e.key == K_5:
                    self.num = 5
                elif e.key == K_6:
                    self.num = 6
                elif e.key == K_7:
                    self.num = 7
                elif e.key == K_8:
                    self.num = 8
                elif e.key == K_9:
                    self.num = 9
