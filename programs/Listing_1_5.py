# base_page.py
import flet as ft

def main(page: ft.Page):
    txt1 = ft.Text("Страница приложения")
    txt2 = ft.Text("Здесь может находиться любой контент")
    col = ft.Column(controls=[txt1, txt2],)
    page.add(col)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)