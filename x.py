import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import matplotlib.pyplot as plt

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        
        # Variables de control
        self.image_path = tk.StringVar()
        self.img_original = None
        self.img_display = None
        self.fusion_image = None
        self.brightness_value = tk.DoubleVar(value=1.0)
        self.contrast_value = tk.DoubleVar(value=1.0)
        self.rotation_value = tk.IntVar(value=0)
        self.transparency_value = tk.DoubleVar(value=1.0)

        # Crear UI
        self.create_widgets()

    def create_widgets(self):
        # Campo de texto para mostrar la ruta de la imagen
        tk.Entry(self.root, textvariable=self.image_path, width=50).pack(pady=5)

        # Botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Explorar", command=self.load_image).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cargar", command=self.display_image).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Actualizar", command=self.update_image).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Guardar", command=self.save_image).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Fusionar Imágenes", command=self.fuse_images).grid(row=0, column=4, padx=5)

        # Controles deslizantes
        tk.Label(self.root, text="Brillo").pack(pady=5)
        tk.Scale(self.root, from_=0.1, to=2.0, orient="horizontal", variable=self.brightness_value).pack(pady=5)
        
        tk.Label(self.root, text="Contraste").pack(pady=5)
        tk.Scale(self.root, from_=0.1, to=2.0, orient="horizontal", variable=self.contrast_value).pack(pady=5)
        
        tk.Label(self.root, text="Rotación").pack(pady=5)
        tk.Scale(self.root, from_=0, to=360, orient="horizontal", variable=self.rotation_value).pack(pady=5)
        
        tk.Label(self.root, text="Transparencia de Fusión").pack(pady=5)
        tk.Scale(self.root, from_=0.0, to=1.0, orient="horizontal", variable=self.transparency_value).pack(pady=5)

        # Área de imagen
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=5)

    def load_image(self):
        image_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if image_file:
            self.image_path.set(image_file)
            self.img_original = Image.open(image_file)
            self.display_image()

    def display_image(self):
        if self.img_original:
            self.img_display = self.img_original.copy()
            img_tk = ImageTk.PhotoImage(self.img_display)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

    def update_image(self):
        if self.img_original:
            # Aplicar brillo y contraste
            enhancer_brightness = ImageEnhance.Brightness(self.img_original)
            enhanced_image = enhancer_brightness.enhance(self.brightness_value.get())
            
            enhancer_contrast = ImageEnhance.Contrast(enhanced_image)
            enhanced_image = enhancer_contrast.enhance(self.contrast_value.get())
            
            # Rotar imagen
            rotated_image = enhanced_image.rotate(self.rotation_value.get())
            
            # Actualizar la imagen mostrada
            self.img_display = rotated_image
            img_tk = ImageTk.PhotoImage(self.img_display)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

    def save_image(self):
        if self.img_display:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
            if save_path:
                self.img_display.save(save_path)

    def fuse_images(self):
        second_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if second_image_path:
            second_image = Image.open(second_image_path).resize(self.img_display.size)
            self.fusion_image = Image.blend(self.img_display, second_image, alpha=self.transparency_value.get())
            
            # Mostrar la imagen fusionada
            img_tk = ImageTk.PhotoImage(self.fusion_image)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
