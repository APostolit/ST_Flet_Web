# BottomSheet_3.py
import flet as ft

def main(page: ft.Page):
    page.title = "Нижний лист"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_switch_change(e: ft.Event[ft.Switch]):
        sheet.fullscreen = e.control.value

    sheet = ft.BottomSheet(
        fullscreen=True,
        show_drag_handle=True,
        content=ft.Container(
            padding=ft.Padding.all(10),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Text("Это содержимое нижнего листа!"),
                          ft.Button("Выход", on_click=lambda: page.pop_dialog()),],
                ),
            ),
        )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[ft.Button(content="Показать нижний лист",
                                    on_click=lambda e: page.show_dialog(sheet),),
                          ft.Switch(value=True,
                                    label="На весь экран",
                                    on_change=handle_switch_change,),
                          ],
                )
            ),
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)