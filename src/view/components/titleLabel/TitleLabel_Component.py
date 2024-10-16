import tkinter as tk
from .TitleLabel_Controller import TitleLabelController

class TitleLabelComponent(tk.Label):
  titleLabelController: TitleLabelController

  def __init__(self):
    self.init_config()

  def init_config(self):
    super().__init__(self, text="Visor de imágenes", font=("Helvetica", 16))
    self.pack(side="top", pady=10)
