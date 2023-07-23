import drawsvg as draw
def draw_line(stt_x, stt_y, end_x, end_y, color='orange'):
    return draw.Line(stt_x, stt_y, end_x, end_y, cw=True, stroke=color, stroke_width=1)
def draw_arc(radius, degree_start, degree_end, color='yellow'):
    return draw.Arc(0, 0, radius, degree_start, degree_end, 
             cw=True, stroke=color, stroke_width=1, fill='none')
def text(text, x_position, y_position):
    return draw.Text(text=text, font_size=12, x=x_position, y=y_position, fill='green', center=True)
import math
def rotate_cartesian(origin, x, y, angle_degrees):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    if origin == None:
        origin = (0, 0)
    ox, oy = origin
    angle = math.radians(angle_degrees)
    qx = ox + math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy)
    qy = oy + math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy)
    return qx, qy