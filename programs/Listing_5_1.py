# AlertDialog_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog"
    d = ft.AlertDialog(
        title=ft.Text("Заголовок окна"),
        content=ft.Text("Основной текст окна."),
        actions=[ft.TextButton("Кнопка")],
        open=True,)
    page.add(d)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)