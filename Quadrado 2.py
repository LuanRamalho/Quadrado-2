from turtle import *
def  quadrado(lado):
    #Desenha um triangulo de lado.
    color('black', 'green')
    begin_fill()
    for i in range(3):
        forward(lado)
        left(90)
    end_fill()
quadrado(220)
done()
