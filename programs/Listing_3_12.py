# CupertinoFilledButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка CupertinoFilledButton"
    page.add(
        ft.SafeArea(
            content=ft.CupertinoFilledButton(
                opacity_on_click=0.3,
                on_click=lambda _: print("Кнопка нажата!"),
                content=ft.Text("Кнопка"),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)