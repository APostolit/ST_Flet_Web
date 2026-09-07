# TimePicker_1
from datetime import time
import flet as ft

def main(page: ft.Page):
    page.title = "TimePicker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e: ft.Event[ft.TimePicker]):
        selection.value = f"Выбрано: {time_picker.value}"
        page.show_dialog(ft.SnackBar(f"Выбрано время: {time_picker.value}"))

    def handle_dismissal(e: ft.Event[ft.DialogControl]):
        page.show_dialog(ft.SnackBar("TimePicker закрыт!"))

    def handle_entry_mode_change(e: ft.TimePickerEntryModeChangeEvent):
        page.show_dialog(ft.SnackBar(f"Изменен режим входа: {time_picker.entry_mode}"))

    time_picker = ft.TimePicker(
        value=time(hour=19, minute=30),
        confirm_text="Подтвердить",
        error_invalid_text="Время вне диапазона",
        help_text="Выбор времени",
        entry_mode=ft.TimePickerEntryMode.DIAL,
        on_change=handle_change,
        on_dismiss=handle_dismissal,
        on_entry_mode_change=handle_entry_mode_change,)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Button(key="pick_time_button",
                                    content="Выбор времени",
                                    icon=ft.Icons.TIME_TO_LEAVE,
                                    on_click=lambda: page.show_dialog(time_picker),),
                          selection := ft.Text(weight=ft.FontWeight.BOLD),],),
            ),
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)