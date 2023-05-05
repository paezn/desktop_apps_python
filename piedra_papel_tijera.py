#------------------------------------
# Desktop app Piedra, Papel y Tijera
#------------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
import random

#-------------------------
# funciones de la app
#-------------------------

# piedra
def escoger_piedra():
    t_resultados.delete("1.0","end")
    usuario = "Piedra"
    lb_user_img.config(image=img_piedra)
    # bt_piedra.config(state="disabled")
    maquina = escoger_maquina()
    if maquina == usuario:
        lb_maq_img.config(image=img_piedra)
        t_resultados.insert(INSERT, f"EMPATE -> Usuario: {usuario} - Máquina: {maquina}")  
    elif maquina =="Papel":
        lb_maq_img.config(image=img_papel)
        t_resultados.insert(INSERT, f"PERDISTE -> Usuario: {usuario} - Máquina: {maquina}")  
    else:
        lb_maq_img.config(image=img_tijera)
        t_resultados.insert(INSERT, f"GANASTE -> Usuario: {usuario} - Máquina: {maquina}")  

    
# papel
def escoger_papel():
    t_resultados.delete("1.0","end")
    usuario = "Papel"
    lb_user_img.config(image=img_papel)
    maquina = escoger_maquina()
    if maquina == usuario:
        lb_maq_img.config(image=img_papel)
        t_resultados.insert(INSERT, f"EMPATE -> Usuario: {usuario} - Máquina: {maquina}")  
    elif maquina =="Piedra":
        lb_maq_img.config(image=img_piedra)
        t_resultados.insert(INSERT, f"GANASTE -> Usuario: {usuario} - Máquina: {maquina}")  
    else:
        lb_maq_img.config(image=img_tijera)
        t_resultados.insert(INSERT, f"PERDISTE -> Usuario: {usuario} - Máquina: {maquina}")

# tijera
def escoger_tijera():
    t_resultados.delete("1.0","end")
    usuario = "Tijera"
    lb_user_img.config(image=img_tijera)
    maquina = escoger_maquina()
    if maquina == usuario:
        lb_maq_img.config(image=img_tijera)
        t_resultados.insert(INSERT, f"EMPATE -> Usuario: {usuario} - Máquina: {maquina}")  
    elif maquina =="Piedra":
        lb_maq_img.config(image=img_piedra)
        t_resultados.insert(INSERT, f"PERDISTE -> Usuario: {usuario} - Máquina: {maquina}")  
    else:
        lb_maq_img.config(image=img_papel)
        t_resultados.insert(INSERT, f"GANASTE -> Usuario: {usuario} - Máquina: {maquina}")

# escoger máquina
def escoger_maquina():
    opciones_maquina = ["Piedra", "Papel", "Tijera"]
    maquina = random.choice(opciones_maquina)
    return maquina

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Temperatura 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#--------------------------------
# variables globales
#--------------------------------
global usuario
global maquina
global img_piedra 
global img_papel
global img_tijera
global img_interrogante

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/piedra_papel_tijera.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=64,y=19)

# creamos los objetos para cada imagen
img_piedra = PhotoImage(file="img/piedra.png")
img_papel = PhotoImage(file="img/papel.png")
img_tijera = PhotoImage(file="img/tijera.png")
img_interrogante = PhotoImage(file="img/interrogante.png")

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=120)
frame_operaciones.place(x=10, y=200)

# boton para sumar

bt_piedra = Button(frame_operaciones,image=img_piedra, command=escoger_piedra)
bt_piedra.place(x=45, y=10, width=100, height=100)

# boton para borrar
bt_papel = Button(frame_operaciones, image=img_papel, command=escoger_papel)
bt_papel.place(x=190, y=10, width=100, height=100)

# boton para salir
bt_tijera = Button(frame_operaciones,image=img_tijera, command=escoger_tijera)
bt_tijera.place(x=335, y=10, width=100, height=100)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=160)
frame_resultados.place(x=10, y=330)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 12))
t_resultados.place(x=10,y=10,width=460,height=30)

# selección usuario
lb_user = Label(frame_resultados, text="Usuario:")
lb_user.config(bg="white", font=("Arial", 20))
lb_user.place(x=16,y=50)

lb_user_img = Label(frame_resultados, image=img_interrogante, bg="white")
lb_user_img.place(x=132,y=50)

# selección maquina
lb_maq = Label(frame_resultados, text="Máquina:")
lb_maq.config(bg="white", font=("Arial", 20))
lb_maq.place(x=248,y=50)

lb_maq_img = Label(frame_resultados, image=img_interrogante, bg="white")
lb_maq_img.place(x=364,y=50)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()