# Button_8.py
import flet as ft

def main(page: ft.Page):
    page.title = "Анимация кнопок"
    def animate(e: ft.Event[ft.Button]):
        e.control.rotate = 0.1 if e.data else 0

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(
                        content="Кнопка с анимацией",
                        rotate=0,
                        animate_rotation=100,
                        on_hover=animate,
                        on_click=lambda e: page.add(
                            ft.Text("Кликнул! Попробуйте удержать")
                        ),
                        on_long_press=lambda e: page.add(
                            ft.Text("Кнопка была удержана!")
                        ),
                    )
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)