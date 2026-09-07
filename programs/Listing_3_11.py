# CupertinoButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка CupertinoButton"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.CupertinoButton(
                        bgcolor=ft.CupertinoColors.LIGHT_BACKGROUND_GRAY,
                        opacity_on_click=0.3,
                        on_click=lambda _: print("Нажато - Обычная кнопка"),
                        content=ft.Text(
                            value="Обычная кнопка",
                            color=ft.CupertinoColors.DESTRUCTIVE_RED,),),
                    ft.CupertinoButton(
                        bgcolor=ft.Colors.PRIMARY,
                        alignment=ft.Alignment.TOP_LEFT,
                        border_radius=ft.BorderRadius.all(15),
                        opacity_on_click=0.5,
                        on_click=lambda _: print("Нажато - Кнопка с заливкой"),
                        content=ft.Text("Кнопка с заливкой",
                                        color=ft.Colors.YELLOW,),),
                    ft.CupertinoButton(
                        bgcolor=ft.Colors.PRIMARY,
                        disabled=True,
                        alignment=ft.Alignment.TOP_LEFT,
                        opacity_on_click=0.5,
                        content=ft.Text("Отключенная кнопка"),
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)