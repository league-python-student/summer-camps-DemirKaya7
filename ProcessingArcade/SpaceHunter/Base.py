class Base:

    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.hp = 5
        self.img = loadImage("base.jpg")
        self.img.resize(150, 150)
        self.collision_radius = 75

    def draw(self):
        image(self.img, self.x, self.y)
