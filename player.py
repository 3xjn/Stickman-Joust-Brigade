import arcade

class Player():    
    def __init__(self, position={"x": 0, "y": 0}, sprite=arcade.Sprite()):
        self.position = position
        self.sprite = sprite

    def draw(self):
        print(self.position)
        self.sprite.center_x = self.position["x"]
        self.sprite.center_y = self.position["y"]
        self.sprite.draw()
        