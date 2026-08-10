from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

keys = set()

def press(key):
    keys.add(key)

def release(key):
    keys.discard(key)

def update():
    if "w" in keys:
        jim.forward(10)
    if "s" in keys:
        jim.backward(10)
    if "a" in keys:
        jim.left(10)
    if "d" in keys:
        jim.right(10)

    screen.ontimer(update, 25)

def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

def press_w():
    press("w")

def release_w():
    release("w")

def press_s():
    press("s")

def release_s():
    release("s")

def press_a():
    press("a")

def release_a():
    release("a")

def press_d():
    press("d")

def release_d():
    release("d")

screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")
screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")
screen.onkeypress(press_a, "a")
screen.onkeyrelease(release_a, "a")
screen.onkeypress(press_d, "d")
screen.onkeyrelease(release_d, "d")
screen.onkey(clear, "c")

screen.listen()
update()
screen.exitonclick()
