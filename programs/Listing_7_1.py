# Badge_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Badge"
    b = ft.FilledIconButton(
        icon=ft.Icons.PHONE,
        badge=ft.Badge(label="3"),
    )
    page.add(b)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)