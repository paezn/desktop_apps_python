#---------------------------------
# Desktop app No. 3- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# sumar
def convertir():
    # borrar salida
    t_resultados.delete("1.0","end")
    messagebox.showinfo("Temperatura 1.0", "Conversión realizada")
    cent = int(c.get())
    if k.get()==1:
        kel = cent + 273.15
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {kel} °K")
    if f.get() == 1:
        far = cent*9/5 + 32
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {far} °F")
    if k.get()==0 and f.get() == 0:
        t_resultados.insert(INSERT, "Debe seleccionar al menos una opción")
    
# borrar
def borrar():
    messagebox.showinfo("Temperatura 1.0", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Temperatura 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

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
c = StringVar()
k = IntVar()
f = IntVar()

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/temperatura.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Termperatura 1.0")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# etiqueta para valor en centigrados
lb_c = Label(frame_entrada, text = "°C = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=240, y=60)

# caja de texto para valor en centigrados
entry_c = Entry(frame_entrada, textvariable=c)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_c.focus_set()
entry_c.place(x=300,y=60)

# chechbox para kelvin
cb_k = Checkbutton(frame_entrada, text="Kelvin", variable=k)
cb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
cb_k.place(x=240, y=110)

# checkbox para farenheit
cb_f = Checkbutton(frame_entrada, text="Fahrenheit", variable=f)
cb_f.config(bg="white", fg="blue", font=("Helvetica", 18))
cb_f.place(x=240, y=140)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para sumar
bt_convertir = Button(frame_operaciones,text="Convertir", command=convertir)
bt_convertir.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()