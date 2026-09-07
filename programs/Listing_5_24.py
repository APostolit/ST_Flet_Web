# TimePicker_3
from datetime import time
import flet as ft

def main(page: ft.Page):
    page.title = "TimePicker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=ft.Button(
                key="custom_locale_button",
                content="Выбор времени (Русский)",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: page.show_dialog(
                    ft.TimePicker(
                        value=time(hour=19, minute=30),
                        locale=ft.Locale("ru", "Русский"),
                    )
                ),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)