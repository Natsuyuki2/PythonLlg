import turtle as t
t.color('red')
U=0
def Carré(N):
    for l in range(4) :
        t.forward(N)
        t.left(90)
        t.done
for m in range(3) :
    for i in range(4) :
        N=60
        Carré(N)
        t.up()
        t.forward(75)
        t.down()
        t.done
    t.up()
    U=U+75
    t.goto(0,U)
    t.down()