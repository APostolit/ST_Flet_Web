# Listing_10_16 - страница "Настройки"
import flet as ft

def create_v():
    txt = ft.Text(value="Страница 'Настройки!'", size=24)
    img = ft.Image(src="images/set.png")
    view = ft.View(controls=[txt, img])
    return view