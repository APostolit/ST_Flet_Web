# DatePicker_2
import datetime
import flet as ft

def main(page: ft.Page):
    page.title = "Календарь с локализацией"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    current_date = datetime.datetime(year=2025, month=4, day=15)

    page.add(
        ft.SafeArea(
            content=ft.Button(
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda _: page.show_dialog(
                    ft.DatePicker(
                        locale=ft.Locale("ru", "Русский"),
                        first_date=datetime.datetime(year=2024, month=1, day=1),
                        last_date=datetime.datetime(year=2026, month=12, day=31),
                        current_date=current_date,
                    )
                ),
                content="Выбор даты (язык русский)",
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)