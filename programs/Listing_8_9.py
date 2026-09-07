# Container_3
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент - Container"

    def handle_hover(e: ft.Event[ft.Container]):
        e.control.bgcolor = ft.Colors.BLUE if e.data else ft.Colors.RED
        e.control.update()

    page.add(
        ft.SafeArea(
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
                width=200,
                height=200,
                bgcolor=ft.Colors.RED,
                ink=False,
                on_hover=handle_hover,
                content=ft.Text("Контейнер",
                                color=ft.Colors.WHITE, size=24),
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)