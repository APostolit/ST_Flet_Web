# FilledIconButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка FilledIconButton"

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    ft.FilledIconButton(icon=ft.Icons.CHECK),
                    ft.FilledIconButton(icon=ft.Icons.ALARM),
                    ft.FilledIconButton(icon=ft.Icons.BOOK),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)