from pygame import *

init()

def displayText(text, surface, size, position, color):
    Font = font.Font('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', size)
    write = Font.render(text, True, color)
    rect = write.get_rect()
    rect.center = position
    surface.blit(write,rect)

class Button(sprite.Sprite):
    def __init__(self, text, dimensions, textSize, position, parent, bgColor=(200,200,200), hColor=(120,120,120), tColor=(0,0,0), pColor=(60,60,60)):
        self.bgColor = bgColor
        self.hColor = hColor
        self.tColor = tColor
        self.pColor = pColor
        self.state = False
        self.color = (0,0,0)
        self.textSize = textSize
        self.parent = parent
        self.dimensions = dimensions
        self.text = text
        self.rect = Rect((0,0), self.dimensions)
        self.rect.center = position
        self.image = self.parent.subsurface(self.rect)

    def isPressed(self):
        if self.isOn() and mouse.get_pressed()[0]:
            return True
        return False

    def isClicked(self, events):
        if self.isOn():
            for e in events:
                if e.type == MOUSEBUTTONUP:
                    return True
        return False

    def isOn(self):
        objPos = self.image.get_abs_offset()
        mousePos = mouse.get_pos()
        if mousePos[0] > objPos[0] and mousePos[0] < objPos[0] + self.dimensions[0] and mousePos[1] > objPos[1] and mousePos[1] < objPos[1] + self.dimensions[1]:
            return True
        return False

    def getState(self):
        return self.state

    def update(self, events):
        if self.isPressed():
            self.color = self.pColor
        elif self.isOn():
            self.color = self.hColor
        else:
            self.color = self.bgColor
        self.state = self.isClicked(events)
        self.image.fill(self.color)
        displayText(self.text, self.image, self.textSize, (self.dimensions[0]/2, self.dimensions[1]/2), self.tColor)



class CheckBox(sprite.Sprite):
    def __init__(self, text, size, position, parent, bgColor=(150,150,150), cColor=(50,50,50)):
        sprite.Sprite.__init__(self)
        self.state = -1
        self.text = text
        self.bgColor = bgColor
        self.cColor = cColor
        self.parent = parent
        self.position = position
        self.size = size
        self.boxRect = Rect((0,0), (size,size))
        self.boxRect.center = position
        self.box = self.parent.subsurface(self.boxRect)
        self.check = Surface((self.size*.7,self.size*.7))
        self.checkRect = self.check.get_rect()
        self.checkRect.center = (self.size/2, self.size/2)

    def getState(self):
        if self.state == 1:
            return True
        return False

    def update(self, events):
        displayText(self.text, self.parent, int(self.size/2), (self.position[0], self.position[1] - self.size), (0,0,0))
        if self.isOn():
            for e in events:
                if e.type == MOUSEBUTTONUP:
                    self.state *= -1
        self.box.fill(self.bgColor)
        self.check.fill(self.cColor)
        if self.state == 1:
            self.box.blit(self.check,self.checkRect)

    def isOn(self):
        objPos = self.box.get_abs_offset()
        mousePos = mouse.get_pos()
        if mousePos[0] > objPos[0] and mousePos[0] < objPos[0] + self.size and mousePos[1] > objPos[1] and mousePos[1] < objPos[1] + self.size:
            return True
        return False
