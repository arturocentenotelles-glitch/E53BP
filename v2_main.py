import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def abrir_registro():
    vr = tk.Toplevel()
    vr.title("Registro")
    vr.geometry("400x300")

    ttk.Label(vr, text="Registro de Usuario", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(vr, text="Nombre:").pack()
    entry_nombre = ttk.Entry(vr, width=30)
    entry_nombre.pack(pady=5)
    ttk.Label(vr, text="Correo:").pack()
    entry_correo = ttk.Entry(vr, width=30)
    entry_correo.pack(pady=5)
    ttk.Label(vr, text="Contraseña:").pack()
    entry_contra = ttk.Entry(vr, width=30, show="*")
    entry_contra.pack(pady=5)
    ttk.Button(vr, text="Continuar").pack(pady=15)

v = tk.Tk()
v.title("Bienvenido")
v.geometry("500x520")

imagen = Image.open("imagen.png")
imagen = imagen.resize((300, 200))
img = ImageTk.PhotoImage(imagen)

tk.Label(v, image=img).pack(pady=10)
ttk.Label(v, text="Software sobre la Adicción a las Redes Sociales", font=("Arial", 14, "bold")).pack(pady=10)
ttk.Label(v, text="Objetivo: Identificar hábitos de uso excesivo y crear conciencia.", font=("Arial", 11), justify="center").pack(pady=20)
ttk.Button(v, text="Ir al registro", command=abrir_registro).pack(pady=10)

v.mainloop()
