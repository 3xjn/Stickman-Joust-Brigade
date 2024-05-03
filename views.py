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
        
        # self.player = Player([10, 10], )
        # self.player.textures = []
        
    def on_draw(self):
        print("Drawing")
        
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        self.player.draw()
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = c.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -c.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -c.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = c.MOVEMENT_SPEED
        
        
def main():
    window = StickmanWindow()
    window.setup()
    arcade.run()