import flet as ft

def create_col():
    txt = ft.Text(value="Домашняя страница!", size=24)
    img = ft.Image(src="images/home.png")
    col = ft.Column(controls=[txt, img])
    return col