import flet as ft

def create_col():
    txt = ft.Text(value="Страница настройки!", size=24)
    img = ft.Image(src="images/set.png")
    col = ft.Column(controls=[txt, img])
    return col