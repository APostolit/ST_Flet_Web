# CupertinoRadio_1
import flet as ft

def main(page: ft.Page):
    page.title = "Выбор CupertinoRadio"
    message = ft.Text()

    group = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.CupertinoRadio(value="red",
                                  label="Красный - Cupertino радио кнопка",
                                  active_color=ft.Colors.RED,
                                  inactive_color=ft.Colors.RED,),
                ft.Radio(value="green",
                         label="Зеленый - Material радио кнопка",
                         fill_color=ft.Colors.GREEN, ),
                ft.Radio(value="blue",
                         label="Голубой - Adaptive радио кнопка",
                         adaptive=True,
                         active_color=ft.Colors.BLUE,),
                ],
            )
        )

    def handle_button_click(_: ft.Event[ft.Button]):
        message.value = f"Выбран цвет: {group.value}"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Выберите цвет:"),
                    group,
                    ft.Button(content="Принять", on_click=handle_button_click),
                    message,
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)