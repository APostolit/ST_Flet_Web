# Container_4
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент - Container"
    def animate_container(e: ft.Event[ft.Container]):
        container.content.size = 24 if container.content.size == 14 else 14
        container.width = 100 if container.width == 200 else 200
        container.height = 50 if container.height == 200 else 200
        container.bgcolor = (
            ft.Colors.BLUE if container.bgcolor == ft.Colors.RED else ft.Colors.RED)
        container.update()

    page.add(
        ft.SafeArea(container := ft.Container(
                        alignment=ft.Alignment.CENTER,
                        width=100,
                        height=50,
                        bgcolor=ft.Colors.RED,
                        on_hover=animate_container,
                        content=ft.Text("Контейнер",
                                        color=ft.Colors.WHITE, size=14),
                        animate=ft.Animation(
                            duration=1000, curve=ft.AnimationCurve.BOUNCE_OUT ),),
                    )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)