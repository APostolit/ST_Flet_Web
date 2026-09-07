# FilledTonalIconButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка FilledIconButton"

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    ft.FilledTonalIconButton(icon=ft.Icons.BRUSH),
                    ft.FilledTonalIconButton(icon=ft.Icons.PHONE),
                    ft.FilledTonalIconButton(icon=ft.Icons.FACE),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)