# TextField_7
import flet as ft

def main(page: ft.Page):
    page.title = "Text"
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = (
            "Значения текстовых полей: "
            f"'{prefix_field.value}', "
            f"'{suffix_field.value}', "
            f"'{prefix_suffix_field.value}', "
            f"'{color_field.value}'."
        )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    prefix_field := ft.TextField(
                        key="prefix_field",
                        label="С префиксом",
                        prefix="https://",
                    ),
                    suffix_field := ft.TextField(
                        key="suffix_field",
                        label="С суффиксом",
                        suffix=".com",
                    ),
                    prefix_suffix_field := ft.TextField(
                        key="prefix_suffix_field",
                        label="С префиксом и суффиксом",
                        prefix="https://",
                        suffix=".com",
                        enable_interactive_selection=True,
                    ),
                    color_field := ft.TextField(
                        key="color_field",
                        label="Указать цвет",
                        icon=ft.Icons.FORMAT_SIZE,
                        hint_text="Синий",
                        helper="Вы можете ввести только один цвет",
                        counter="{value_length}/{max_length} символов",
                        prefix_icon=ft.Icons.COLOR_LENS,
                        suffix="...ваш цвет",
                        max_length=20,
                    ),
                    ft.Button(
                        key="submit_button",
                        content="Принять",
                        on_click=handle_button_click,
                    ),
                    message := ft.Text(),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)