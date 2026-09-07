# DatePicker_1
import datetime
import flet as ft

def main(page: ft.Page):
    page.title = "Календарь"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    messages = ft.Column(tight=True)

    def handle_change(e: ft.Event[ft.DatePicker]):
        messages.controls.append(
            ft.Text(f"Выбрана дата: {e.control.value.strftime('%m/%d/%Y')}")
        )

    def handle_dismissal(_: ft.Event[ft.DialogControl]):
        messages.controls.append(ft.Text("Календарь закрыт"))

    today = datetime.datetime(year=2025, month=4, day=15)

    picker = ft.DatePicker(
        first_date=datetime.datetime(year=today.year - 1, month=1, day=1),
        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
        current_date=today,
        on_change=handle_change,
        on_dismiss=handle_dismissal,)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Button(icon=ft.Icons.CALENDAR_MONTH,
                                    on_click=lambda _: page.show_dialog(picker),
                                    content="Выберите дату",),
                          messages,],),)
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)