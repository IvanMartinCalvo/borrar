import arcade






def draw_background():
    """Draw the background"""
    arcade.draw_lrtb_rectangle_filled(0, 599, 500, 0, (27, 77, 117))
    arcade.draw_lrtb_rectangle_filled(0, 599, 400, 0, (35, 90, 135))
    arcade.draw_lrtb_rectangle_filled(0, 599, 350, 0, (47,  114, 168))
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

def draw_star(x,y):
    """Dibuja la estrella fugaz"""
    arcade.draw_ellipse_filled(15+x, 450+y, 25, 15, (224, 221, 132))
    arcade.draw_line(0+x, 460+y, 25+x, 450+y, (224, 221, 132))
    arcade.draw_line(0+x, 455+y, 20+x, 457+y, (224, 221, 132))
    arcade.draw_line(0+x, 450+y, 25+x, 451+y, (224, 221, 132))
    arcade.draw_line(0+x, 450+y, 20+x, 448+y, (224, 221, 132))
    arcade.draw_line(0+x, 440+y, 25+x, 445+y, (224, 221, 132))
    arcade.draw_line(0+x, 445+y, 20+x, 450+y, (224, 221, 132))

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    # Fondo
    draw_background()
    # Estrella fugaz
    draw_star(on_draw.estrella_x, on_draw.estrella_y)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.

    on_draw.estrella_x += 5

    for i in range(100):
        on_draw.estrella_y += 0.5
    for i in range(50):
        on_draw.estrella_y -= 0.25
    for i in range(50):
        on_draw.estrella_y += 0.25
    for i in range(100):
        on_draw.estrella_y -= 0.5

# Create a value that our on_draw.snow_person1_x will start at.
on_draw.estrella_x = 0
on_draw.estrella_y = 0

def main():
    arcade.open_window(600, 600, "El polo norte")

    arcade.set_background_color((17, 62, 99))

    arcade.start_render()
    #Fondo
    draw_background()
    #Estrella fugaz
    draw_star(0, 0)

    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

main()



