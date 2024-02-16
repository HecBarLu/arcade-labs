import arcade

# Preparacion Dibujo
arcade.open_window(height=600, width=800, window_title="Skipper")
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()

# Dibujo Suelo
arcade.draw_lrtb_rectangle_filled(left=0, right=800, top=200, bottom=0, color=[240, 248, 255])

# Dibujar al pingüino, Cabeza
arcade.draw_circle_filled(center_x=350, center_y=420, radius=75, color=(0, 0, 0))
arcade.draw_circle_filled(center_x=350, center_y=420, radius=62, color=(250, 235, 215))
arcade.draw_circle_filled(center_x=320, center_y=440, radius=8, color=(0, 0, 0))
arcade.draw_circle_filled(center_x=380, center_y=440, radius=8, color=[0, 0, 0])
arcade.draw_triangle_filled(350, 360, 380, 420, 320, 420, (255, 191, 0))

# Dibujar cuerpo
arcade.draw_ellipse_filled(350, 210, 300, 300, (0, 0, 0), 0, 20)
arcade.draw_ellipse_filled(350, 210, 250, 280, (250, 235, 215), 0, 20)

# Dibujar brazos
arcade.draw_triangle_filled(440, 275, 380, 275, 410, 200, (0, 0, 0))
arcade.draw_triangle_filled(260, 275, 320, 275, 290, 200, (0, 0, 0))

# Dibujar pies
arcade.draw_ellipse_filled(280, 60, 80, 90, (255, 191, 0), 90, 1)
arcade.draw_ellipse_filled(430, 65, 80, 90, (255, 191, 0), 270, 1)

# Dibujar balon
arcade.draw_ellipse_filled(600, 70, 100, 100, (250, 235, 215), 1, 50)
arcade.draw_ellipse_filled(600, 70, 40, 40, (0, 0, 0), 1, 5)
# --- Finish drawing --
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()




