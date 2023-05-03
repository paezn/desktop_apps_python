#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# sumar
def calcular():
    messagebox.showinfo("Minical(culadora 1.0", "Las operaciones han sido realizadas")
    s = int(x.get()) + int(y.get())
    r = int(x.get()) - int(y.get())
    m = int(x.get()) * int(y.get())
    d = int(x.get()) / int(y.get())
    de = int(x.get()) // int(y.get())
    mod = int(x.get()) % int(y.get())
    p = int(x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")


# borrar
def borrar():
    messagebox.showinfo("Minicalculadora 1.0", "Los datos serán borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Minicalculadora 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#--------------------------------
# variables globales
#--------------------------------
x = StringVar()
y = StringVar()

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Minicalculadora 1.0")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# etiqueta para valor de x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290,y=60)

# etiqueta para valor de y
lb_y = Label(frame_entrada, text = "Y = ")
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

# caja de texto para valor y
entry_y = Entry(frame_entrada, textvariable=y)
entry_y.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_y.place(x=290,y=120)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para sumar
bt_sumar = Button(frame_operaciones,text="Calcular", command=calcular)
bt_sumar.place(x=45, y=35, width=100, height=30)

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