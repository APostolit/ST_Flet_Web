# Slider_3
import flet as ft

def main(page: ft.Page):
    page.title = "Slider"
    def slider_changed(e: ft.Event[ft.Slider]):
        message.value = f"Задано значение: {e.control.value}"
        message.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Слайдер с обработчиком событий on_change:"),
                    ft.Slider(
                        key="slider",
                        min=0,
                        max=100,
                        divisions=10,
                        label="{value}%",
                        on_change=slider_changed,
                    ),
                    message := ft.Text(),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)