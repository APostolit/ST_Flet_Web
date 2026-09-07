# base_column.py
import flet as ft

def main(page: ft.Page):
    column = ft.Column(
        width=220,
        height=120,
        spacing=12,
        controls=[
            ft.Text("Строка 1"),
            ft.Text("Строка 2"),
            ft.Text("Строка 3"),
        ],
    )
    page.add(column)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)