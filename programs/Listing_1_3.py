# base_row.py
import flet as ft

def main(page: ft.Page):
    row = ft.Row(
        controls=[
            ft.Text("Строка 1"),
            ft.Text("Строка 2"),
            ft.Text("Строка 3"),
        ],
    )
    page.add(row)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)