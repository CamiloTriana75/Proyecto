from atexit import register
from cProfile import label
import logging
from tkinter import font
import turtle
import time
import random
from tkinter import *
import os

posponer=0.1

#Marcador
puntaje = 0
puntaje_mas_alto = 0

#Ventana
wn = turtle.Screen()
wn.title("juego de la culebrita")
wn.bgcolor("green")
wn.setup(width=700, height=600)
wn.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)


#Cuerpo de la serpiente
segmentos = []


#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje: 0       Puntaje mas alto: 0", align = "center", font =("Courier",24, "normal"))


#Funciones
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label (text="Escoja su opcion", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label (text="").pack()
    Button (text="Acceder", height="2", width="30", bg=pestas_color, command=logging).pack()
    Label (text="").pack
    Button (text="Registrarse", height="2", width="30", bg=pestas_color, command=register) .pack() 
    Label (text="").pack
    ventana_principal.mainloop




def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"        


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)            



#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")



while True:
    wn.update()


    #Colision con la ventana 
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.diretion = "stop"

        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #Limpira lista de segmentos
        segmentos.clear()

        #Resetear marcador
        puntaje = 0
        texto.clear()
        texto.write("Puntaje: {}     Puntaje mas alto: {}".format(puntaje, puntaje_mas_alto),
                align = "center", font =("Courier", 24, "normal"))   


    #Colisiones de la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)


        #Aumentar marcador
        puntaje += 10

        if puntaje > puntaje_mas_alto:
            puntaje_mas_alto = puntaje

        texto.clear()
        texto.write("Puntaje: {}     Puntaje mas alto: {}".format(puntaje, puntaje_mas_alto),
                align = "center", font =("Courier", 24, "normal"))




    #Mover el cuerpo de la serpiente 
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0 ,-1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()
    #Colision con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1) 
            cabeza.goto(0,0)
            cabeza.direction = "stopped"

            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            
            segmentos.clear()


    time.sleep(posponer)











