# first_app.py
import flet as ft

def main(page: ft.Page):
    txt = ft.Text("Привет, Это приложение Flet!🌍")
    page.add(txt)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
    # ft.run(main, view=ft.AppView.WEB_BROWSER, port=8501)
