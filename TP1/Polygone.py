import turtle as t
t.up()
t.goto(0,-200)
t.down()
N=input("Entrer une valeur:")
N=int(N)
for i in range(N):
    t.forward(100)
    t.left(360/N)
    t.done

print("Program Terminated")
