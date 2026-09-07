# TextField_5
import flet as ft

def main(page: ft.Page):
    page.title = "Text"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        key="multiline_standard",
                        label="Стандартное поле",
                        multiline=True,
                    ),
                    ft.TextField(
                        label="Отключенное поле",
                        multiline=True,
                        disabled=True,
                        value="line1\nline2\nline3\nline4\nline5",
                    ),
                    ft.TextField(
                        key="multiline_auto_height",
                        label="Многострочное с полосой прокрутки",
                        multiline=True,
                        min_lines=1,
                        max_lines=3,
                    ),
                ],
            ),
        ),
    )
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)