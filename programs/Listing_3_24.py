# OutlinedButton_2
import flet as ft

def main(page: ft.Page):
    page.title = "OutlinedButton"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_button_click(e: ft.Event[ft.OutlinedButton]):
        button.data += 1
        message.value = f"Кнопка нажата {button.data} раз(а)"
        page.update()

    button = ft.OutlinedButton(
        content="Нажмите на кнопку",
        data=0,
        on_click=handle_button_click,)
    message = ft.Text()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[button, message],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)