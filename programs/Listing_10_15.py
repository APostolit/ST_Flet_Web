# Listing_10_15 - Домашняя страница
import flet as ft

def create_v():
    txt = ft.Text(value="Домашняя страница!", size=24)
    img = ft.Image(src="images/home.png")
    view = ft.View(controls=[txt, img])
    return view