# Button_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка"
    bt1 = ft.Button(content="Активная кнопка")
    bt2 = ft.Button(content="Пассивная кнопка", disabled=True)
    page.add(bt1, bt2)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)