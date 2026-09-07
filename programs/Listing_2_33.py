# TextField_4
import flet as ft

def main(page: ft.Page):
    page.title = "Text"
    page.add(
        ft.SafeArea(
            content=ft.TextField(
                key="password_textfield",
                label="Введите пароль",
                password=True,
                can_reveal_password=True,
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)