import turtle as t
t.bgcolor('black')
t.shape('turtle')
t.speed(0)
t.pensize(50)
t.color('gold')
for x in range(1000):
    if x % 6 == 0:
        t.color('purple')
    if x % 6 == 1:
        t.color('green')
    if x % 6 == 2:
        t.color('sky blue')
    if x % 6 == 3:
        t.color('red')
    if x % 6 == 4:
        t.color('gold')
    if x % 6 == 5:
        t.color('pink')
    t.forward(x*1.2)
    t.left(59)
