import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Bienvenido")
ventana.geometry("500x520")

imagen = Image.open("imagen.png")
imagen = imagen.resize((300, 200))
img = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(ventana, image=img)
label_imagen.pack(pady=10)

titulo = ttk.Label(ventana, text="Software sobre la Adicción a las Redes Sociales", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

objetivo = ttk.Label(ventana, text="Objetivo: Identificar hábitos de uso excesivo y crear conciencia.", font=("Arial", 11), justify="center")
objetivo.pack(pady=20)

ventana.mainloop()
