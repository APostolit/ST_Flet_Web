# BottomAppBar_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Нижняя панель"
    b = ft.BottomAppBar(
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(ft.Icons.MENU),
                ft.IconButton(ft.Icons.SEARCH),
                ft.IconButton(ft.Icons.SETTINGS),
            ],
        ),
    )
    page.bottom_appbar = b

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)