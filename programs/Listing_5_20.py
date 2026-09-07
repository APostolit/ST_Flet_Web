# DateRangePicker_1
import datetime
import flet as ft

def main(page: ft.Page):
    page.title = "Календарь интервал дат"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    messages = ft.Column(tight=True)
    today = datetime.datetime(year=2025, month=6, day=15)

    def handle_change(e: ft.Event[ft.DateRangePicker]):
        messages.controls.extend(
            [ft.Text(f"Начало периода: {e.control.start_value.strftime('%m/%d/%Y')}"),
             ft.Text(f"Конец периода: {e.control.end_value.strftime('%m/%d/%Y')}"),])

    def handle_dismissal(_: ft.Event[ft.DialogControl]):
        messages.controls.append(ft.Text("Календарь сброшен"))

    picker = ft.DateRangePicker(
        start_value=datetime.datetime(year=today.year, month=today.month, day=1),
        end_value=datetime.datetime(year=today.year, month=today.month, day=15),
        first_date=datetime.datetime(year=2024, month=1, day=1),
        last_date=datetime.datetime(year=2026, month=12, day=31),
        current_date=today,
        on_change=handle_change,
        on_dismiss=handle_dismissal,)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Button(icon=ft.Icons.DATE_RANGE,
                                    on_click=lambda _: page.show_dialog(picker),
                                    content="Выбор интервала дат",),
                          messages,],),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)