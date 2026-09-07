# TextField_1
import flet as ft

def main(page: ft.Page):
    page.title = "TextField"
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = (
            f"Введены значения:  '{tb1.value}', '{tb2.value}', "
            f"'{tb3.value}', '{tb4.value}', '{tb5.value}'."
        )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    tb1 := ft.TextField(label="Стандартное поле"),
                    tb2 := ft.TextField(
                        label="Отключенное поле",
                        disabled=True,
                        value="Введите ФИО",
                    ),
                    tb3 := ft.TextField(
                        label="Только для чтения",
                        read_only=True,
                        value="Иванов А.А.",
                    ),
                    tb4 := ft.TextField(
                        label="С заполнителем",
                        hint_text="Введите текст в это поле",
                    ),
                    tb5 := ft.TextField(
                        label="С иконкой",
                        icon=ft.Icons.EMOJI_EMOTIONS,
                    ),
                    ft.Button(content="Принять", on_click=handle_button_click),
                    message := ft.Text(),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)