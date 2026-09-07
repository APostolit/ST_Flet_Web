# TimePicker_2
from datetime import time
import flet as ft

def main(page: ft.Page):
    page.title = "TimePicker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_system_hour_format():
        """Возвращает текущий системный часовой формат."""
        return "24h" if page.media.always_use_24_hour_format else "12h"

    def format_time(value: time) -> str:
        """Возвращает отформатированную строку времени,
        основанную на выборе времени и системных настройках."""
        use_24h = time_picker.hour_format == ft.TimePickerHourFormat.H24 or (
            time_picker.hour_format == ft.TimePickerHourFormat.SYSTEM
            and page.media.always_use_24_hour_format)
        return value.strftime("%H:%M" if use_24h else "%I:%M %p")

    def handle_change(e: ft.Event[ft.TimePicker]):
        selection.value = f"Выбрано время: {format_time(time_picker.value)}"

    time_picker = ft.TimePicker(value=time(hour=19, minute=30),
                                help_text="Выберите время собрания",
                                on_change=handle_change,)

    def open_picker(e: ft.Event[ft.Button]):
        choice = format_dropdown.value
        hour_format_map = {"system": ft.TimePickerHourFormat.SYSTEM,
                           "12h": ft.TimePickerHourFormat.H12,
                           "24h": ft.TimePickerHourFormat.H24,}
        time_picker.hour_format = hour_format_map[choice]
        page.show_dialog(time_picker)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            format_dropdown := ft.Dropdown(
                                label="Часовой формат",
                                value="system",
                                width=260,
                                key="dd",
                                options=[
                                    ft.DropdownOption(
                                        key="system",
                                        text=(f"Системное время "
                                              f"({get_system_hour_format()})"),
                                    ),
                                    ft.DropdownOption(key="12h", text="12-часовой формат"),
                                    ft.DropdownOption(key="24h", text="24-часовой формат"),
                                ],
                            ),
                            ft.Button("Выбор времени",
                                      icon=ft.Icons.SCHEDULE,
                                      on_click=open_picker,),
                        ],
                    ),
                    selection := ft.Text(weight=ft.FontWeight.BOLD),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)