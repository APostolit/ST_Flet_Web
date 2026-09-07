# CupertinoTextField_1
import flet as ft

def main(page: ft.Page):
    page.title = "Текстовое поле"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        label="Текстовое поле Material",
                        label_style=ft.TextStyle(color=ft.Colors.GREY_400),
                    ),
                    ft.CupertinoTextField(
                        placeholder_text=" Текстовое поле Cupertino",
                        placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400),
                    ),
                    ft.TextField(
                        adaptive=True,
                        label="Текстовое поле Adaptive",
                        label_style=ft.TextStyle(color=ft.Colors.GREY_400),
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)