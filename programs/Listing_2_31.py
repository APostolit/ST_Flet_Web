# TextField_2
import flet as ft

def main(page: ft.Page):
    page.title = "TextField"
    def handle_field_change(e: ft.Event[ft.TextField]):
        message.value = e.control.value

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        key="handling_change_textfield",
                        label="Обработка событий",
                        on_change=handle_field_change,
                    ),
                    message := ft.Text(),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)