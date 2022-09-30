import turtle as t
U=0

def Noir(N):
    t.color('black')
    t.begin_fill()
    for l in range(4) :
        t.forward(N)
        t.left(90)
    t.end_fill()
    t.up()
    t.forward(60)
    t.down()

def Blanc(N):
    for l in range(4) :
        t.forward(N)
        t.left(90)
    t.up()
    t.forward(60)
    t.down()

def BlancNoir(N):
    Blanc(N)
    Noir(N)

def NoirBlanc(N):
    Noir(N)
    Blanc(N)

for m in range(3) :
    for i in range(2) :
        N=60
        Noir(N)
        Blanc(N)
        t.done
    t.up()
    U=U+60
    t.goto(0,U)
    t.down()