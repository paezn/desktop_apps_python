#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel centigrados
def abrir_toplevel_centigrados():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Centigrados")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("300x200")
    toplevel_centigrados.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_centigrados, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "°C = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=150, y=60)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_centigrados,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_centigrados.destroy()

# convertir
def convertir():
    messagebox.showinfo("Temperatura 1.0", "Conversión realizada")
    # cent = int(c.get())
    if kf.get()=="kelvin":
        k = cent + 273.15
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {k} °K")
    elif kf.get() == "fahrenheit":
        f = cent*9/5 + 32
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {f} °F")
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")
    
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
kf = StringVar()
global logo

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

# boton para abrir Toplevel para ingresar °C
bt_centigrados = Button(frame_entrada, text="Ingresar °C", command=abrir_toplevel_centigrados)
bt_centigrados.place(x=240, y=60)

# radiobutton para kelvin
rb_k = Radiobutton(frame_entrada, text="Kelvin", variable=kf, value="kelvin")
rb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_k.place(x=240, y=110)

# radiobutton para farenheit
rb_f = Radiobutton(frame_entrada, text="Fahrenheit", variable=kf, value="fahrenheit")
rb_f.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_f.place(x=240, y=140)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir
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