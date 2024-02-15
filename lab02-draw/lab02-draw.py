import arcade

# Preparacion Dibujo
arcade.open_window(height=600, width=800, window_title="Skipper")
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()

# Dibujo Suelo
arcade.draw_lrtb_rectangle_filled(left=0, right=800, top=200, bottom=0, color=[1,2,3])

# Dibujar al pingüino
arcade.draw_circle_filled(center_x=350, center_y=420, radius=75, color=(0, 0, 0))
arcade.draw_circle_filled(center_x=350, center_y=420, radius=62, color=(250, 235, 215))
arcade.draw_circle_filled(center_x=320, center_y=440, radius=8, color=(0, 0, 0))
arcade.draw_circle_filled(center_x=380, center_y=440, radius=8, color=[0, 0, 0])
arcade.draw_parabola_outline(start_x=310, start_y=360, end_x=390, height=30, color=(0, 0, 0), border_width=10,
                             tilt_angle=180)
arcade.draw_triangle_filled(350, 360, 380, 420, 320, 420, (255, 191, 0))

# Dibujar cuerpo
arcade.draw_ellipse_filled(350, 210, 300, 300, (0, 0, 0), 0, 20)
arcade.draw_ellipse_filled(350, 210, 250, 280, (250, 235, 215), 0, 20)
# --- Finish drawing --
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()




