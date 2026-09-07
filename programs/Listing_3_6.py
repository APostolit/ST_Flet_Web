# Button_6.py
import flet as ft

def main(page: ft.Page):
    page.padding = 30
    page.spacing = 30
    page.title = "Формы кнопок"
    bt_1 = ft.Button(content="Стадион",
                     style=ft.ButtonStyle(shape=ft.StadiumBorder()),)
    bt_2 = ft.Button(content="Закругленный прямоугольник",
                     style=ft.ButtonStyle(
                         shape=ft.RoundedRectangleBorder(radius=10)),)
    bt_3 =  ft.Button(content="Непрерывный прямоугольник",
                      style=ft.ButtonStyle(
                          shape=ft.ContinuousRectangleBorder(radius=30)),)
    bt_4 = ft.Button(content="Скошенный прямоугольник",
                     style=ft.ButtonStyle(
                         shape=ft.BeveledRectangleBorder(radius=10)),)
    bt_5 = ft.Button(content="Круг",
                     style=ft.ButtonStyle(
                         shape=ft.CircleBorder(), padding=30),)

    page.add(ft.SafeArea(content=ft.Column(
        controls=[bt_1, bt_2, bt_3, bt_4, bt_5])
            ), )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)