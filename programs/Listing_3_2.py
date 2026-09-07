# Button_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(content="Активная кнопка"),
                    ft.Button(content="Пассивная кнопка", disabled=True),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)