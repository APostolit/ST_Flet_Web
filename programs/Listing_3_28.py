# TextButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Текстовая кнопка"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextButton(content="Текстовая кнопка активная"),
                    ft.TextButton(content="Текстовая кнопка пассивная", disabled=True),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)