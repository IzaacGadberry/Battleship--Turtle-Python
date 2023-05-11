import turtle as t

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Ocean Maker

def gridMaker(wn):
    wn.bgcolor('Black')
    wnTk = wn.getcanvas().winfo_toplevel()
    wnTk.attributes("-fullscreen", True)
    turt = t.Turtle()
    turt.penup()
    wn.addshape('ocean.gif')
    turt.shape('ocean.gif')
    turt.stamp()
    turt.hideturtle()
    