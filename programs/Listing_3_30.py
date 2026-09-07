# TextButton_3
import flet as ft

def main(page: ft.Page):
    page.title = "TextButton обработка событий"

    def button_clicked(e):
        button.data += 1
        message_text.value = f"Кнопка нажата {button.data} раз(а)"

    message_text = ft.Text()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    button := ft.TextButton(
                        key="TextButton",
                        content="Текстовая кнопка",
                        data=0,
                        on_click=button_clicked,),
                    ft.Container(
                        padding=ft.Padding(left=12),
                        content=message_text,
                    ),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)