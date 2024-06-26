import arcade
import constants as c
from player import *

class StickmanWindow(arcade.Window):
    """
    Main application class.
    """
    
    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT,
                         c.SCREEN_TITLE, resizable=True)
        
    def setup(self):
        print("Setting up the game")
        
        self.background = arcade.load_texture("./assets/background.png")
        
        # change player.position to be respective of sprite's position
        self.player = Player({"x": 10, "y": 10}, arcade.Sprite("./assets/run/run1.png"))
        # self.player.textures = []
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player.sprite, gravity_constant=1
        )
        
    def on_draw(self):
        print("Drawing")
        
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        self.player.draw()
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player.position["y"] += c.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.position["y"] -= c.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.position["x"] -= c.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.position["x"] += c.MOVEMENT_SPEED
        
        
def main():
    window = StickmanWindow()
    window.setup()
    arcade.run()