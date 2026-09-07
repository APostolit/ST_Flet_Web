# Slider_1
import flet as ft

def main(page: ft.Page):
    page.title = "Slider"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Слайдер с параметрами по умолчанию:"),
                    ft.Slider(),
                    ft.Text("Не доступный слайдер:"),
                    ft.Slider(disabled=True),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)