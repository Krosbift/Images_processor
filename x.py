import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Mostrar Imagen con Tkinter")

# Cargar la imagen usando PIL
image = Image.open("C:/Users/Torif/OneDrive/Documents/user/code/Images_processor/src/assets/Logo_UTP.png")

# Redimensionar la imagen a un tamaño fijo (por ejemplo, 200x200)
fixed_size = (200, 200)
image = image.resize(fixed_size, Image.LANCZOS)

# Convertir la imagen redimensionada a un objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Crear un widget Label y asignar la imagen
label = tk.Label(root, image=photo)
label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()