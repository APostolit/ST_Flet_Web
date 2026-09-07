# TextField_6
import flet as ft

def main(page: ft.Page):
    page.title = "Text"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        key="underlined_field",
                        label="Подчеркнутое поле",
                        border=ft.InputBorder.UNDERLINE,
                        hint_text="Введите текст в это поле",
                    ),
                    ft.TextField(
                        key="underlined_filled_field",
                        label="Подчеркнутое с заполнением",
                        border=ft.InputBorder.UNDERLINE,
                        filled=True,
                        hint_text="Введите текст в это поле",
                    ),
                    ft.TextField(
                        key="borderless_field",
                        label="Поле без границ",
                        border=ft.InputBorder.NONE,
                        hint_text="Введите текст в это поле",
                    ),
                    ft.TextField(
                        key="borderless_filled_field",
                        label="Без границ с заполнением",
                        border=ft.InputBorder.NONE,
                        filled=True,
                        hint_text="Введите текст в это поле",
                    ),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)