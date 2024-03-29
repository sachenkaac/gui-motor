from tkinter import Tk, Label, Button, PhotoImage
from PIL import Image, ImageTk
from datetime import datetime

# Crear la ventana principal
ventana = Tk()
ventana.geometry("500x500")
ventana.title("GUI Tinkercad")

# Funciones para manejar los eventos de los botones
def izquierda():
    etiqueta.config(text="Estado del motor: Girando en sentido antihorario")
    cargar_gif("izquierda.gif")

def derecha():
    etiqueta.config(text="Estado del motor: Girando en sentido horario")
    cargar_gif("derecha.gif")

def detener():
    etiqueta.config(text="Estado del motor: Detenido")
    cargar_gif("detenido.gif")

def cargar_gif(file):
    gif = Image.open(file)
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif))
            gif.seek(len(frames))  # Avanzar al siguiente frame
    except EOFError:
        pass
    animar_gif(frames)

def animar_gif(frames, index=0):
    gif_label.config(image=frames[index])
    gif_label.image = frames[index]
    ventana.after(100, animar_gif, frames, (index + 1) % len(frames))

def actualizar_fecha_hora():
    fecha_hora_actual = datetime.now().strftime("%H:%M:%S - %Y-%m-%d")
    etiqueta2.config(text=fecha_hora_actual)
    ventana.after(1000, actualizar_fecha_hora)  # Actualizar cada segundo

# Crear una etiqueta para mostrar el estado del motor
etiqueta = Label(ventana, text="Estado del motor: Detenido", font=("Arial Bold", 20), fg="blue")
etiqueta.place(x=0, y=100)

# Crear una etiqueta para mostrar la fecha y hora
etiqueta2 = Label(ventana, text="", font=("Arial Bold", 20), fg="blue")
etiqueta2.place(x=0, y=200)

# Crear una etiqueta para mostrar el GIF
gif_label = Label(ventana)
gif_label.place(x=0, y=300)

# Crear botones con imágenes
imagen_izquierda = PhotoImage(file="flecha-izquierda.png")
boton_izquierda = Button(ventana, image=imagen_izquierda, command=izquierda)
boton_izquierda.place(x=0, y=0)

imagen_detener = PhotoImage(file="pausa.png")
boton_detener = Button(ventana, image=imagen_detener, command=detener)
boton_detener.place(x=100, y=0)

imagen_derecha = PhotoImage(file="flecha-correcta.png")
boton_derecha = Button(ventana, image=imagen_derecha, command=derecha)
boton_derecha.place(x=200, y=0)

# Actualizar la fecha y hora
actualizar_fecha_hora()

# Ejecutar el bucle de eventos
ventana.mainloop()
