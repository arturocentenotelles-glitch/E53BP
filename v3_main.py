import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def abrir_test():
    vt = tk.Toplevel()
    vt.title("Test")
    vt.geometry("650x600")

    ttk.Label(vt, text="Test de Adicción a Redes Sociales", font=("Arial", 16, "bold")).pack(pady=10)

    preguntas = [
        "1. ¿Cuánto tiempo usas redes sociales al día?",
        "2. ¿Te distraes en actividades importantes?",
        "3. ¿Te sientes ansioso sin el celular?",
        "4. ¿Revisas redes al despertar?",
        "5. ¿Te desvelas por redes?",
        "6. ¿Afecta tus tareas?",
        "7. ¿Ignoras personas por usar redes?",
        "8. ¿Publicas buscando atención?",
        "9. ¿Te urge responder mensajes?",
        "10. ¿Te molesta no recibir reacciones?"
    ]

    opciones = ["Nunca", "A veces", "Frecuentemente"]
    vars_respuestas = []

    for p in preguntas:
        frame = ttk.LabelFrame(vt, text=p)
        frame.pack(fill="x", padx=10, pady=5)
        var = tk.StringVar(value="")
        vars_respuestas.append(var)
        for op in opciones:
            ttk.Radiobutton(frame, text=op, variable=var, value=op).pack(anchor="w")

v = tk.Tk()
v.title("Bienvenido")
v.geometry("500x520")

imagen = Image.open("imagen.png")
imagen = imagen.resize((300, 200))
img = ImageTk.PhotoImage(imagen)

tk.Label(v, image=img).pack(pady=10)
ttk.Label(v, text="Software sobre la Adicción a las Redes Sociales", font=("Arial", 14, "bold")).pack(pady=10)
ttk.Button(v, text="Abrir Test", command=abrir_test).pack(pady=20)

v.mainloop()
