import turtle

def draw_fractal():
    window = turtle.Screen()
    window.bgcolor('yellow')

    pin = turtle.Turtle()
    pin.color('black', 'green')


    
    cell_rep = 20
    def cell():
        pin.fill(True)
        pin.setheading(120)
        pin.forward(cell_rep)
        pin.setheading(-120)
        pin.forward(cell_rep)
        pin.fill(False)

    def tissue(x):
        for i in range(x):
            if x == 3:
                if i == 1:
                    pin.color('yellow')
                    pin.setheading(180)
                    pin.forward(cell_rep)
                    pin.color('black', 'green')
                else:
                    cell()
            else:
                cell()
    def origin():
        count = 1
        pin.setheading(120)
        pin.forward(cell_rep*4)
        pin.setheading(-120)
        while count <= 4:
            pin.forward(cell_rep)
            pin.setheading(0)
            pin.forward(count * cell_rep)
            tissue(count)
            count += 1

    def draw_fractal(num):
        y = 1
        while  y <= num:
            pin.setheading(-120)
            pin.forward(cell_rep * 4)
            pin.setheading(0)
            pin.forward(y * cell_rep * 4)
            for m in range(y):
                origin()
            pin.setheading(0)
            y += 1

    draw_fractal(5)

    
    
    print pin.position()

    window.exitonclick()

draw_fractal()