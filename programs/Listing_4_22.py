# Slider_2
import flet as ft

def main(page: ft.Page):
    page.title = "Slider"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Слайдер со значением:"),
                    ft.Slider(value=0.3),
                    ft.Text("Слайдер с заданным диапазоном и надписью:"),
                    ft.Slider(min=0, max=100, divisions=10, label="{value}%"),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)