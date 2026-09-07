# BottomSheet_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "Нижний лист"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_sheet_dismissal(e: ft.Event[ft.DialogControl]):
        page.add(ft.Text("Закрыли нижний лист"))

    sheet = ft.BottomSheet(
        on_dismiss=handle_sheet_dismissal,
        content=ft.Container(
            padding=50,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                controls=[ft.Text("Содержимой нижнего листа!"),
                          ft.Button("Выход", on_click=lambda _: page.pop_dialog()),],
                ),
            ),
        )
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(content="Показать нижний лист",
                              on_click=lambda e: page.show_dialog(sheet),)
                    ]
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)