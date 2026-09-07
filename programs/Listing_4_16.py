# Radio_1
import flet as ft

def main(page: ft.Page):
    page.title = "Radio"
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = f"Выбран цвет:  {group.value}"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Сделайте выбор цвета:"),
                    group := ft.RadioGroup(
                        content=ft.Column(
                            controls=[
                                ft.Radio(key="basic_radio_red",
                                         value="red", label="Красный"),
                                ft.Radio(value="green", label="Зеленый"),
                                ft.Radio(value="blue", label="Синий"),
                            ]
                        )
                    ),
                    ft.Button(key="basic_submit_button",
                              content="Выбрать",
                              on_click=handle_button_click,),
                    message := ft.Text(),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)