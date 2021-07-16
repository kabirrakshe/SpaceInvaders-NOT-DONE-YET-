class character():
    def __init__(self, x, y, surface, image, speed):
        self.x = x
        self.y = y
        self.surface = surface
        self.surfacewidth, self.surfaceheight = self.surface.get_width(), self.surface.get_height()
        self.image = image
        self.speed = speed
    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
    def moveRight(self):
        self.x += self.speed
    def moveLeft(self):
        self.x -= self.speed
    def moveUp(self):
        self.y -= self.speed
    def moveDown(self):
        self.y += self.speed
    def reset(self):
        self.x = self.surfacewidth //2
        self.y = self.surfaceheight // 2
