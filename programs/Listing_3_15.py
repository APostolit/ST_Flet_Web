# CupertinoTintedButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка CupertinoTintedButton"
    bt = ft.CupertinoTintedButton("Кнопка")
    page.add(bt)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)