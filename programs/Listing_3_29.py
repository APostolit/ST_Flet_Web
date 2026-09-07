# TextButton_2
import flet as ft

def main(page: ft.Page):
    page.title = "TextButtons с иконкой"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        content="Кнопка с иконкой",
                        icon=ft.Icons.WAVES_OUTLINED,
                    ),
                    ft.TextButton(
                        content="Кнопка с цветной иконкой",
                        icon=ft.Icons.PARK_ROUNDED,
                        icon_color=ft.Colors.GREEN_400,
                    ),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)