# OutlinedButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "OutlinedButton"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.OutlinedButton(content="Доступная кнопка"),
                         ft.OutlinedButton(content="Недоступная кнопка", disabled=True),]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)