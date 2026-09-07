# AppBar_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Верхняя панель инструментов"
    b = ft.AppBar(
        leading=ft.Icon(ft.Icons.MENU),
        title=ft.Text("Верхняя панель"),
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ],
    )
    page.add(b)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)