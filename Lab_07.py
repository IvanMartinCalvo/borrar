import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10
DEAD_ZONE = 0.02

class Ball:
    def __init__(self, position_x, position_y, change_x,change_y , radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color((17, 62, 99))


        self.set_mouse_visible(False)
        # Create our ball
        self.ball = Ball(50, 50,0,0, 15, arcade.color.AUBURN)

        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 599, 500, 0, (27, 77, 117))
        arcade.draw_lrtb_rectangle_filled(0, 599, 400, 0, (35, 90, 135))
        arcade.draw_lrtb_rectangle_filled(0, 599, 350, 0, (47, 114, 168))
        arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (61, 111, 186))
        arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, (208, 245, 245))
        arcade.draw_circle_filled(500, 550, 40, (224, 221, 132))
        arcade.draw_circle_filled(20, 130, 40, (194, 209, 209))
        arcade.draw_lrtb_rectangle_filled(0, 599, 130, 0, (208, 245, 245))
        arcade.draw_lrtb_rectangle_filled(0, 599, 120, 0, (190, 232, 232))
        arcade.draw_lrtb_rectangle_filled(-10, 70, 130, 110, (194, 209, 209))
        arcade.draw_ellipse_filled(35, 110, 70, 10, (194, 209, 209))
        arcade.draw_lrtb_rectangle_outline(20, 40, 145, 135, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(10, 30, 135, 125, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(0, 10, 135, 125, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(30, 50, 135, 125, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(5, 25, 125, 115, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(0, 5, 125, 115, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(0, 20, 145, 135, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(5, 25, 125, 115, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(5, 25, 155, 145, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(25, 45, 155, 145, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(40, 58, 145, 135, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(25, 45, 125, 115, (143, 181, 181))
        arcade.draw_lrtb_rectangle_outline(45, 65, 125, 115, (143, 181, 181))
        arcade.draw_circle_filled(200, 400, 5, (208, 245, 245))
        arcade.draw_circle_filled(150, 370, 5, (208, 245, 245))
        arcade.draw_circle_filled(300, 350, 5, (208, 245, 245))
        arcade.draw_circle_filled(250, 300, 5, (208, 245, 245))
        arcade.draw_circle_filled(550, 400, 5, (208, 245, 245))
        arcade.draw_circle_filled(400, 400, 5, (208, 245, 245))
        self.ball.draw()

    def update(self, delta_time):

        # Update the position according to the game controller
        if self.joystick:
            print(self.joystick.x, self.joystick.y)

            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED
        self.ball.update()



def main():
    window = MyGame(SCREEN_HEIGHT, SCREEN_WIDTH , "Drawing Example")

    arcade.run()


main()