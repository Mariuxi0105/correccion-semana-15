import math
import os
import tkinter as tk
from typing import Optional

from PIL import Image, ImageChops, ImageTk


RUTA_ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


def cargar_logo(
    master: tk.Misc,
    dimension_maxima: int,
    foreground: str,
    background: Optional[str] = None,
) -> tk.Image:
    rutas_png = (
        os.path.join(RUTA_ASSETS, "logo_restaurante.png"),
        os.path.join(RUTA_ASSETS, "logo-restaurante.png"),
        os.path.join(RUTA_ASSETS, "logo_restaurante.jpg"),
        os.path.join(RUTA_ASSETS, "logo-restaurante.jpg"),
        os.path.join(RUTA_ASSETS, "logo_restaurante.jpeg"),
        os.path.join(RUTA_ASSETS, "logo-restaurante.jpeg"),
    )
    ruta_png = next((ruta for ruta in rutas_png if os.path.isfile(ruta)), None)
    if ruta_png is not None:
        with Image.open(ruta_png) as imagen_original:
            imagen = imagen_original.convert("RGB")
        fondo = Image.new("RGB", imagen.size, "white")
        diferencia = ImageChops.difference(imagen, fondo).convert("L")
        limites = diferencia.point(lambda pixel: 255 if pixel > 18 else 0).getbbox()
        if limites:
            imagen = imagen.crop(limites)
        imagen.thumbnail(
            (dimension_maxima, dimension_maxima), Image.Resampling.LANCZOS
        )
        return ImageTk.PhotoImage(imagen, master=master)

    opciones = {"master": master, "file": os.path.join(RUTA_ASSETS, "logo_restaurante.xbm"), "foreground": foreground}
    if background:
        opciones["background"] = background
    return tk.BitmapImage(**opciones)