import arcade

class Player():    
    def __init__(self, position=[0,0], sprite=arcade.Sprite()):
        self.position = position
        self.sprite = sprite

    def draw(self):
        self.sprite.center_x = self.position[0]
        self.sprite.center_y = self.position[1]
        self.sprite.draw()
        