import turtle as tl

tl.speed(15)
tl.color('black')
for i in range(0, 15):
    for y in range(0, 5):
        if y == 0:
            tl.fillcolor('magenta')
        elif y == 1:
            tl.fillcolor('yellow')
        elif y == 2:
            tl.fillcolor('red')
        elif y == 3:
            tl.fillcolor('green')
        elif y == 4:
            tl.fillcolor('orange')
        tl.begin_fill()
        tl.circle(200, 115)
        tl.left(65)
        tl.circle(200, 115)
        tl.left(180)
        tl.end_fill()
